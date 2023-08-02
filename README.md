# Alkahest: Schema Interconversion Project

## Trinary Interconversion Between DBML, SQLAlchemy, and Python Classes

This document provides a reference to translate between three prevalent constructs in database schema management: Database Markup Language (DBML), SQLAlchemy (a Python library), and Python Classes. The ability to interconvert these constructs aids in translating a DBML schema into SQLAlchemy code, converting Python classes into DBML notation, and vice versa.

This guide has been updated to include a new architecture based on Python classes, which provides a more structured and extensible way to represent and translate database schemas.

### Python Classes for Schema Representation

In the new architecture, each concept in a database schema (such as a table, column, or constraint) is represented by a Python class. Each class has methods to convert that concept to DBML, SQLAlchemy, or SQL.

Here are the main classes:

- `Entry`: This is the base class for all other classes. It provides the basic structure for a database concept, including methods to translate to DBML, SQLAlchemy, and SQL.

- `Table`: This class represents a table in a database schema.

- `Column`: This class represents a column in a table.

- `DataType`: This class represents a data type for a column.

- `NullableColumn`, `DefaultColumn`, `PrimaryKeyColumn`, `ForeignKeyColumn`: These classes represent different types of columns with specific properties.

- `CheckConstraint`: This class represents a check constraint in a table.

Each of these classes can be used to create objects representing components of your database schema. You can then use the methods of these objects to get the DBML, SQLAlchemy, or SQL representation.

### Using the Classes

To use the classes, first create an object for each component of your schema. For example, to create a `Table` object, you would do something like this:

```python
table = Table('molecules', 'Chemistry')
```

You can then use the methods of the object to get the DBML, SQLAlchemy, or SQL representation:

```python
print(table.to_dbml())
print(table.to_sqlalchemy())
print(table.to_sql())
```

This approach is more flexible and maintainable than the previous dictionary-based approach. It allows for more complex behavior, better type checking, and improved IDE support.

### Trinary Interconversion

The term "trinary" refers to something composed of three parts. In this case, it refers to the interconversion between DBML, SQLAlchemy, and Python Classes. By using Python classes as a "bridge", we can translate seamlessly between these three constructs, making it easier to manage and manipulate database schemas.