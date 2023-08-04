from lark import Lark, Transformer, v_args
from alkahest_classes import Database, Schema, Table, Column, DataType, ForeignKey, View, Enum

# Defining the grammar
dbml_grammar = """
    start: project
    project: "Project" STRING "{" (table | view | enum)* "}"
    table: "Table" table_name "{" (column | foreign_key)* "}"
    table_name: SCHEMA_NAME "." STRING
    column: STRING data_type settings?
    data_type: STRING
    settings: "[" setting ("," setting)* "]"
    setting: "pk" | "increment"
    foreign_key: "Ref:" STRING "<" STRING
    view: "View" STRING "As" "SQL" MULTILINE_STRING "End"
    enum: "Enum" STRING "{" value ("," value)* "}"
    value: STRING
    SCHEMA_NAME: CNAME
    %import common.CNAME
    %import common.STRING
    %import common.MULTILINE_STRING
    %import common.WS
    %ignore WS
"""

class DBMLTransformer(Transformer):
    """
    Transformer class for parsing DBML into Database, Schema, Table, Column, DataType, ForeignKey, and View objects.
    """

    def start(self, items):
        """
        Transforms the start of the DBML syntax.

        Args:
            items (list): List of parsed tokens.

        Returns:
            list: Transformed list of tokens.
        """
        return items[0]
    
    def project(self, items):
        """
        Transforms the project section of the DBML syntax into a Database object.

        Args:
            items (list): List of parsed tokens.

        Returns:
            Database: Transformed Database object.
        """
        return Database(name=items[0], schemas=items[1:])
    
    def table(self, items):
        """
        Transforms the table section of the DBML syntax into a Schema object.

        Args:
            items (list): List of parsed tokens.

        Returns:
            Schema: Transformed Schema object.
        """
        schema_name, table_name = items[0].split(".")
        if len(items[0].split(".")) != 2:
            raise ValueError(f"Expected schema_name.table_name, got {items[0]}")
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
        """
        Transforms the column section of the DBML syntax into a Column object.

        Args:
            items (list): List of parsed tokens.

        Returns:
            Column: Transformed Column object.
        """
        return Column(name=items[0], data_type=DataType(dbml=items[1], sqlalchemy="", sql=""), nullable="not null" not in items[2:], primary_key="pk" in items[2:])
    
    def data_type(self, items):
        """
        Transforms the data type section of the DBML syntax.

        Args:
            items (list): List of parsed tokens.

        Returns:
            str: Transformed data type.
        """
        return items[0]
    
    def settings(self, items):
        """
        Transforms the settings section of the DBML syntax.

        Args:
            items (list): List of parsed tokens.

        Returns:
            list: Transformed list of settings.
        """
        return items
    
    def foreign_key(self, items):
        """
        Transforms the foreign key section of the DBML syntax into a ForeignKey object.

        Args:
            items (list): List of parsed tokens.

        Returns:
            ForeignKey: Transformed ForeignKey object.
        """
        table, column = items[0].split(".")
        return ForeignKey(table=table, column=column, ref_table=items[1].split(".")[0], ref_column=items[1].split(".")[1])
    
    def view(self, items):
        """
        Transforms the view section of the DBML syntax into a View object.

        Args:
            items (list): List of parsed tokens.

        Returns:
            View: Transformed View object.
        """
        schema_name, view_name = items[0].split(".")
        return View(name=view_name, sql=items[1])
    
    def enum(self, items):
        """
        Transforms the enum section of the DBML syntax into a Enum object.

        Args:
            items (list): List of parsed tokens.

        Returns:
            Enum: Transformed Enum object.
        """
        return Enum(name=items[0], values=items[1:])

def create_parser():
    """
    Creates a Lark parser for DBML.

    Returns:
        Lark: The Lark parser for DBML.
    """
    return Lark(dbml_grammar, start='start', parser='lalr')

@v_args(inline=True)
def parse_dbml(dbml_string, parser):
    """
    Parses a DBML string into a tree using a Lark parser.

    Args:
        dbml_string (str): The DBML string to parse.
        parser (Lark): The Lark parser to use.

    Returns:
        Tree: The resulting tree after parsing the DBML string.
    """
    return parser.parse(dbml_string)

def transform_dbml(tree, transformer):
    """
    Transforms a parsed DBML tree into a Database object using a DBMLTransformer.

    Args:
        tree (Tree): The parsed DBML tree.
        transformer (DBMLTransformer): The DBMLTransformer to use.

    Returns:
        Database: The resulting Database object after transforming the DBML tree.
    """
    return transformer.transform(tree)
