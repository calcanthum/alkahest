from lark import Lark, Transformer
from alkahest_classes import Database, Schema, Table, Column, DataType, ForeignKey, View

# Defining the grammar
dbml_grammar = """
    start: project
    project: "Project" STRING "{" (table | view)+ "}"  # Added view here
    table: "Table" table_name "{" (column | foreign_key)+ "}"
    table_name: SCHEMA_NAME "." STRING
    column: STRING data_type settings?
    data_type: STRING
    settings: "[" setting ("," setting)* "]"
    setting: "pk" | "increment"
    foreign_key: "Ref:" STRING "<" STRING
    view: "View" STRING "As" "SQL" MULTILINE_STRING "End"  # Added this line for views
    SCHEMA_NAME: CNAME
    %import common.CNAME
    %import common.STRING
    %import common.MULTILINE_STRING  # Added this line to import MULTILINE_STRING
    %import common.WS
    %ignore WS
"""

class DBMLTransformer(Transformer):
    """
    The DBMLTransformer class extends the Transformer class from the Lark library.
    It provides methods to transform parsed DBML elements into Alkahest objects.

    This class uses the transformer design pattern to convert one representation of data into another.
    Methods:
    -------
    start(items: List) -> Any:
        Transforms the start of the DBML syntax.

    project(items: List) -> Database:
        Transforms the project section of the DBML syntax into a Database object.

    table(items: List) -> Schema:
        Transforms the table section of the DBML syntax into a Schema object.

    column(items: List) -> Column:
        Transforms the column section of the DBML syntax into a Column object.

    data_type(items: List) -> str:
        Transforms the data type section of the DBML syntax.

    settings(items: List) -> List:
        Transforms the settings section of the DBML syntax.

    foreign_key(items: List) -> ForeignKey:
        Transforms the foreign key section of the DBML syntax into a ForeignKey object.

    view(items: List) -> View:
        Transforms the view section of the DBML syntax into a View object.
    """
    def start(self, items):

        return items[0]
    
    def project(self, items):

        return Database(name=items[0], schemas=items[1:])
    
    def table(self, items):
        schema_name, table_name = items[0].split(".")
        columns = []
        foreign_keys = []
        for item in items[1:]:
            if isinstance(item, Column):
                columns.append(item)
            elif isinstance(item, ForeignKey):
                foreign_keys.append(item)
        table = Table(name=table_name, columns={column.name: column for column in columns})
        for fk in foreign_keys:
            table.columns[fk.column].foreign_keys = [fk]
        return Schema(name=schema_name, tables=[table])
    
    def column(self, items):
        return Column(name=items[0], data_type=DataType(dbml=items[1], sqlalchemy="", sql=""), nullable="not null" not in items[2:], primary_key="pk" in items[2:])
    
    def data_type(self, items):
        return items[0]
    
    def settings(self, items):
        return items
    
    def foreign_key(self, items):
        table, column = items[1].split(".")
        return ForeignKey(table=table, column=column)
    
    def view(self, items):
        schema_name, view_name = items[0].split(".")
        return View(name=view_name, sql=items[1])

# Instantiate the Lark parser with the DBML grammar and transformer
dbml_parser = Lark(dbml_grammar, parser='lalr', transformer=DBMLTransformer())