# Alkahest: Schema Interconversion Project
## Interconversion Between DBML, SQLAlchemy, and SQL

Alkahest is a Python library that provides a comprehensive reference to translate between three prevalent languages in database schema management: Database Markup Language (DBML), SQLAlchemy (a Python library), and SQL. The ability to interconvert these languages aids in translating a DBML schema into SQLAlchemy code, converting SQL commands into DBML notation, and vice versa. 

The Alkahest project includes four key classes: `DataType`, `Alkahest`, `Table`, and `Column`. Each class represents a component of a database and knows how to represent itself in DBML, SQLAlchemy, and SQL.

## Alkahest Class

The `Alkahest` class represents a database. It has two attributes: `name`, which is the name of the database, and `tables`, which is a dictionary of `Table` objects that represent the tables in the database.

## Table Class

The `Table` class represents a table in a database. It has two attributes: `name`, which is the name of the table, and `columns`, which is a dictionary of `Column` objects that represent the columns in the table.

## Column Class

The `Column` class represents a column in a table. It has several attributes:

- `name`: The name of the column.
- `data_type`: A `DataType` object that represents the data type of the column.
- `nullable`: A boolean that indicates whether the column is nullable. The default is `False`.
- `default_value`: The default value of the column. The default is `None`.
- `primary_key`: A boolean that indicates whether the column is a primary key. The default is `False`.
- `foreign_key`: The reference for a foreign key. The default is `None`.

## DataType Class

The `DataType` class represents a data type in a column. It has three attributes: `dbml`, `sqlalchemy`, and `sql`, which are the names of the data type in DBML, SQLAlchemy, and SQL, respectively.

By creating instances of these classes and using the provided methods, you can easily translate a database schema from one language to another.