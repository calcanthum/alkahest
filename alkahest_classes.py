from dataclasses import dataclass, field
from typing import Dict, List, Optional

@dataclass
class DataType:
    """
    DataType class represents a data type in a column.

    Attributes:
        dbml (str): The name of the data type in DBML.
        sqlalchemy (str): The name of the data type in SQLAlchemy.
        sql (str): The name of the data type in SQL.
    """
    dbml: str
    sqlalchemy: str
    sql: str

@dataclass
class ForeignKey:
    """
    ForeignKey class represents a foreign key in a column.

    Attributes:
        table (str): The name of the table the foreign key references.
        column (str): The name of the column the foreign key references.
    """
    table: str
    column: str

@dataclass
class Column:
    """
    Column class represents a column in a table.

    Attributes:
        name (str): The name of the column.
        data_type (DataType): The data type of the column.
        nullable (bool): Whether the column is nullable.
        default_value (Any): The default value of the column.
        primary_key (bool): Whether the column is a primary key.
        foreign_keys (List[ForeignKey]): The list of foreign keys. The default is an empty list.
    """
    name: str
    data_type: DataType
    nullable: bool = True
    primary_key: bool = False
    default_value = None
    unique: bool = False
    check: str = None
    exclude: str = None
    foreign_keys: Optional[List[ForeignKey]] = None

@dataclass
class Relationship:
    """A class to represent a relationship between two tables in a database."""
    table1: str
    table2: str
    foreign_keys: List[ForeignKey]

@dataclass
class Table:
    """
    Table class represents a table in a database.

    Attributes:
        name (str): The name of the table.
        columns (Dict[str, 'Column']): A dictionary of columns in the table.
    """
    name: str
    columns: Dict[str, Column]
    relationships: List[Relationship] = None

@dataclass
class Enum:
    name: str
    values: List[str]

@dataclass
class View:
    """A class to represent a view in a database."""
    name: str
    columns: Dict[str, Column]
    query: str

@dataclass
class Schema:
    """
    Schema class represents a schema in a database.

    Attributes:
        name (str): The name of the schema.
        tables (Dict[str, 'Table']): A dictionary of tables in the schema.
    """
    name: str
    tables: Dict[str, 'Table'] = field(default_factory=dict)

@dataclass
class Database:
    """
    Database class represents a database.

    Attributes:
        name (str): The name of the database.
        schemas (Dict[str, 'Schema']): A dictionary of schemas in the database.
    """
    name: str
    schemas: Dict[str, 'Schema'] = field(default_factory=dict)