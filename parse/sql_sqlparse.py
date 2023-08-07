import sqlparse
from sqlparse.sql import Identifier, Function, Parenthesis
from sqlparse.tokens import Keyword, DML
from alkahest_classes import Database, Schema, Table, Column, DataType, Enum, View, ForeignKey

class SQLtoAlkahest:
    def __init__(self, sql_string, default_schema="public"):
        """
        Initialize the SQLtoAlkahest parser.
        
        Args:
        - sql_string (str): The SQL string to be parsed.
        - default_schema (str, optional): The default schema to use if not provided. Defaults to "public".
        """
        self.sql_string = sql_string
        self.statements = sqlparse.parse(sql_string)
        self.database = Database()  # Create a new Database object to store the parsed schema
        self.current_schema = self.database.schemas.setdefault(default_schema, Schema(name=default_schema))

    def parse(self):
        """
        Parse the SQL statements.
        """
        for statement in self.statements:
            if statement.get_type() == "CREATE":
                if "TABLE" in statement.value:
                    self.handle_create_table(statement)
                elif "TYPE" in statement.value:
                    self.handle_create_type(statement)
                elif "VIEW" in statement.value:
                    self.handle_create_view(statement)

    def handle_create_table(self, statement):
        """
        Handle CREATE TABLE statements.
        
        Args:
        - statement (sqlparse.sql.Statement): The SQL statement to be parsed.
        """
        table_name = None
        columns = []
        for token in statement.tokens:
            if token.ttype is sqlparse.tokens.Name:
                table_name = token.value
            elif isinstance(token, sqlparse.sql.Parenthesis):
                columns = self.process_columns(token)
        
        table = Table(name=table_name, columns=columns)
        self.current_schema.tables[table_name] = table

    def process_columns(self, token):
        """
        Extract column details from a given Parenthesis token.
        
        Args:
        - token (sqlparse.sql.Parenthesis): The token to be processed.

        Returns:
        - list: A list of Column objects.
        """
        columns = []
        for item in token.get_sublists():
            if isinstance(item, sqlparse.sql.Identifier):
                column_name = item.get_real_name()
                data_type = item.get_parent_name().split()[0]  # Get the first word of the parent name as the data type
                
                if "REFERENCES" in item.get_parent_name():
                    ref_tables_columns = item.get_parent_name().split("REFERENCES ")[-1].split(", ")
                    ref_tables = [table_column.split()[0] for table_column in ref_tables_columns]
                    ref_columns = [table_column.split()[1] for table_column in ref_tables_columns]
                    foreign_key = ForeignKey(tables=ref_tables, columns=ref_columns)
                else:
                    foreign_key = None
                
                columns.append(Column(name=column_name, data_type=DataType(dbml=data_type, sqlalchemy="", sql=""), foreign_key=foreign_key))
        return columns

    def handle_foreign_key(self, identifier):
        """
        Handle FOREIGN KEY constraints.
        
        Args:
        - identifier (sqlparse.sql.Identifier): The identifier containing the foreign key information.
        """
        fk_info = identifier.value.partition("FOREIGN KEY")[-1].strip()
        table_name, column_name = fk_info.strip("()").split()
        foreign_key = ForeignKey(table=table_name, column=column_name)
        self.current_schema.tables[table_name].columns[column_name].foreign_key = foreign_key

    def handle_create_type(self, statement):
        """
        Handle CREATE TYPE (enums) statements.
        
        Args:
        - statement (sqlparse.sql.Statement): The SQL statement to be parsed.
        """
        enum_name = next(token for token in statement.tokens if isinstance(token, Identifier)).get_real_name()
        enum_values = next(token.value for token in statement.tokens if isinstance(token, Parenthesis))
        enum = Enum(name=enum_name, values=enum_values)
        self.current_schema.enums[enum_name] = enum

    def handle_create_view(self, statement):
        """
        Handle CREATE VIEW statements.
        
        Args:
        - statement (sqlparse.sql.Statement): The SQL statement to be parsed.
        """
        view_name = next(token for token in statement.tokens if isinstance(token, Identifier)).get_real_name()
        sql_query = " ".join(token.value for token in statement.tokens if not isinstance(token, (Identifier, Keyword.DDL)))
        view = View(name=view_name, sql=sql_query)
        self.current_schema.views[view_name] = view
