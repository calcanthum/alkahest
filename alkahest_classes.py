from dataclasses import dataclass, field
from typing import Dict, List, Optional

@dataclass
class DataType:
    """
    Represents the data type of a column in a database table.

    Attributes:
        dbml: The data type in DBML format.
        sqlalchemy: The data type in SQLAlchemy format.
        sql: The data type in SQL format.
    """
    dbml: str
    sqlalchemy: str
    sql: str

@dataclass
class View:
    name: str
    sql: str

@dataclass
class ForeignKey:
    """
    Represents a foreign key constraint in a database table.

    Attributes:
        table: The name of the table that the foreign key references.
        column: The name of the column that the foreign key references.
    """
    table: str
    column: str

@dataclass
class Column:
    """
    Represents a column in a database table.

    Attributes:
        name: The name of the column.
        data_type: The data type of the column.
        nullable: Whether the column allows NULL values.
        primary_key: Whether the column is a primary key.
        default_value: The default value for the column.
        unique: Whether the column values must be unique.
        check: Any CHECK constraints for the column.
        exclude: Any EXCLUDE constraints for the column.
        foreign_keys: Any foreign keys for the column.
        table: A reference to the table that the column belongs to.
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
    table: 'Table' = None  

@dataclass
class Relationship:
    """
    Represents a relationship between two tables in a database.

    Attributes:
        table1: The name of the first table in the relationship.
        table2: The name of the second table in the relationship.
        column1: The column in the first table involved in the relationship.
        column2: The column in the second table involved in the relationship.
        foreign_keys: The foreign keys defining the relationship.
    """
    table1: str
    table2: str
    column1: Column = None  
    column2: Column = None  
    foreign_keys: List[ForeignKey]

@dataclass
class Table:
    """
    Represents a table in a database.

    Attributes:
        name: The name of the table.
        columns: A dictionary mapping column names to Column objects.
        relationships: The relationships involving the table.
    """
    name: str
    columns: Dict[str, Column]
    relationships: List[Relationship] = None

@dataclass
class Enum:
    """
    Represents an enumeration in a database.

    Attributes:
        name: The name of the enumeration.
        values: The values of the enumeration.
    """
    name: str
    values: List[str]

@dataclass
class View:
    """
    Represents a view in a database.

    Attributes:
        name: The name of the view.
        columns: The columns in the view.
        query: The SQL query that defines the view.
    """
    name: str
    columns: List[Column] = field(default_factory=list)  
    query: str

@dataclass
class Schema:
    """
    Represents a schema in a database.

    Attributes:
        name: The name of the schema.
        tables: The tables in the schema.
    """
    name: str
    tables: List[Table] = field(default_factory=list)  


@dataclass
class Database:
    """
    Represents a database.

    Attributes:
        name: The name of the database.
        schemas: The schemas in the database.
    """
    name: str
    schemas: List[Schema] = field(default_factory=list)  