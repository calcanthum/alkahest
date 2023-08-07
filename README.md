
# Alkahest

Alkahest is a Python-based project designed to act as a universal translation layer between DBML (Database Markup Language), SQL, and SQLAlchemy. The primary purpose of Alkahest is to translate your database schema between different formats, helping to keep your documentation (DBML, Markdown) in sync with your actual database (SQL, SQLAlchemy). 

This project was born out of the need to maintain the AlembIQ database and keep its documentation synchronized. However, the functionality of Alkahest extends beyond this use case, as it can serve any project that requires similar work to be done.

## Features

- **Translation between PostgreSQL, SQLAlchemy, and DBML**: Alkahest can translate between these three representations of a database, assisting in keeping all representations synchronized.
- **Python classes for representing databases**: Alkahest provides a set of Python classes that can represent the components of a database, such as columns, tables, schemas, and the database itself.
- **Markdown documentation support**: Each Alkahest class includes a `notes` attribute that can hold Markdown documentation for the represented database component. This feature allows for inline, human-readable documentation that can be easily updated and accessed.

## Project Structure

The project consists of a set of custom Python classes representing the elements of a database schema, a set of functions that translate these elements between DBML, SQL, and SQLAlchemy, and a Lark-based parser that transforms DBML schemas into Alkahest objects.

1. **alkahest_classes.py**: This file contains the definitions of various classes that represent the different elements of a database schema. These include `Database`, `Schema`, `Table`, `Column`, `DataType`, `ForeignKey`, `Relationship`, and `View`.

2. **alkahest_functions.py**: This file contains the `Translator` class, which handles the translation of Alkahest objects (as defined in `alkahest_classes.py`) into their appropriate representations in DBML, SQL, and SQLAlchemy.

3. **dbml_lark.py**: This file uses the Lark library to parse DBML strings into Alkahest objects.

## Usage

### Setup
To use Alkahest, you'll first need to import the necessary classes and functions:

```python
from alkahest_classes import Database, Schema, Table, Column, DataType
from alkahest_functions import Translator
```

### Examples
Let's create a simplified version of the AlembIQ database schema using Alkahest classes:

```python
# Define data types
integer = DataType('integer')
varchar = DataType('varchar')

# Define some columns
id_column = Column('id', integer)
name_column = Column('name', varchar)

# Define a table
table = Table('Lab', [id_column, name_column])

# Define a schema
schema = Schema('LabManagement', [table])

# Define a database
database = Database('AlembIQ', [schema])
```

Now, we can use the Translator class to convert this to DBML:

```python
translator = Translator()
dbml = translator.to_dbml(database)
print(dbml)
```

This will output:

```markdown
Project AlembIQ {
  Schema LabManagement {
    Table Lab {
      id integer
      name varchar
    }
  }
}
```

## Documentation

For a detailed description of the Alkahest architecture and classes, please visit the Wiki.

## Feedback and Contributions

Alkahest is an ongoing project and is continuously evolving. Feedback, suggestions, and contributions are always welcome.

## Why "Alkahest"?

The name is derived from an alchemical universal solvent, having the power to dissolve every other substance, including gold.

Alkahest represents the ability to dissolve the barriers between different representations of a database schema — DBML, SQL, SQLAlchemy, and Markdown. Just as the mythical solvent was thought to be capable of reducing all compounds into their original elements, the Alkahest project reduces a database schema into its basic elements (tables, columns, relationships, etc.) and transforms them into different formats.
