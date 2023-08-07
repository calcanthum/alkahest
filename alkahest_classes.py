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
        notes (Optional[str], default=None): Markdown notes about the data type.
    """
    dbml: str
    sqlalchemy: str
    sql: str
    notes: Optional[str] = None

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
        notes (Optional[str], default=None): Markdown notes about the column.
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
    notes: Optional[str] = None

@dataclass
class Relationship:
    """
    Represents a relationship between two tables in a database.

    Attributes:
        table1: The name of the first table in the relationship.
        table2: The name of the second table in the relationship.
        column1: The name of the column in the first table involved in the relationship.
        column2: The name of the column in the second table involved in the relationship.
        foreign_keys: The foreign keys defining the relationship.
        notes (Optional[str], default=None): Markdown notes about the relationship.
    """
    table1: str
    table2: str
    column1: str = None
    column2: str = None
    foreign_keys: List[ForeignKey]
    notes: Optional[str] = None

@dataclass
class Table:
    """
    Represents a table in a database.

    Attributes:
        name: The name of the table.
        columns: A dictionary mapping column names to Column objects.
        relationships: The relationships involving the table.
        schema: The schema the table belongs to
        notes (Optional[str], default=None): Markdown notes about the table.
    """
    name: str
    columns: Dict[str, Column]
    relationships: List[Relationship] = None
    schema: str
    notes: Optional[str] = None

@dataclass
class ForeignKey:
    """
    Represents a foreign key constraint in a database table.

    Attributes:
        table: The names of the tables that the foreign key references.
        column: The names of the columns that the foreign key references.
        notes (Optional[str], default=None): Markdown notes about the foreign key constraint.
    """
    tables: List[Table] = None
    columns: List[Column] = None
    notes: Optional[str] = None

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
        notes (Optional[str], default=None): Markdown notes about the view.
    """
    name: str
    columns: List[Column] = field(default_factory=list)
    query: str
    notes: Optional[str] = None

@dataclass
class Schema:
    """
    Represents a schema in a database.

    Attributes:
        name: The name of the schema.
        tables: The tables in the schema.
        notes (Optional[str], default=None): Markdown notes about the schema.
    """
    name: str
    tables: List[Table] = field(default_factory=list)
    notes: Optional[str] = None


@dataclass
class Database:
    """
    Represents a database.

    Attributes:
        name: The name of the database.
        schemas: The schemas in the database.
        notes (Optional[str], default=None): Markdown notes about the database.
    """
    name: str
    schemas: List[Schema] = field(default_factory=list)
    notes: Optional[str] = None