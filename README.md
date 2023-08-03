# Alkahest: Schema Interconversion Project
## Interconversion Between DBML, SQLAlchemy, and SQL

Alkahest is a Python library that provides a comprehensive reference to translate between three prevalent languages in database schema management: Database Markup Language (DBML), SQLAlchemy (a Python library), and SQL. The ability to interconvert these languages aids in translating between schema descriptions. 

The Alkahest project includes six key classes: `Alkahest`, `Schema`, `Table`, `Column`, `DataType`, and `ForeignKey`. Each class represents a component of a database (or an entire database) and knows how to represent itself in DBML, SQLAlchemy, and SQL.

## Alkahest Class

The `Alkahest` class represents a database. It has two attributes: `name`, which is the name of the database, and `schemas`, which is a dictionary of `Schema` objects that represent the schemas in the database.

## Schema Class

The `Schema` class represents a schema in a database. It has two attributes: `name`, which is the name of the schema, and `tables`, which is a dictionary of `Table` objects that represent the tables in the schema.

## Table Class

The `Table` class represents a table in a database. It has two attributes: `name`, which is the name of the table, and `columns`, which is a dictionary of `Column` objects that represent the columns in the table.

## Column Class

The `Column` class represents a column in a table. It has several attributes:

- `name`: The name of the column.
- `data_type`: A `DataType` object that represents the data type of the column.
- `nullable`: A boolean that indicates whether the column is nullable. The default is `False`.
- `default_value`: The default value of the column. The default is `None`.
- `primary_key`: A boolean that indicates whether the column is a primary key. The default is `False`.
- `foreign_keys`: A list of `ForeignKey` objects. The default is an empty list.

## ForeignKey Class

The `ForeignKey` class represents a foreign key in a column. It has three attributes:

- `name`: The name of the foreign key.
- `table`: The name of the table the foreign key references.
- `column`: The name of the column the foreign key references.

## DataType Class

The `DataType` class represents a data type in a column. It has three attributes: `dbml`, `sqlalchemy`, and `sql`, which are the names of the data type in DBML, SQLAlchemy, and SQL, respectively.
