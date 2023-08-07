# Alkahest
*A universal translation layer for database schemas.*

Alkahest is a Python-based project designed to act as a universal translation layer between DBML (Database Markup Language), SQL, and SQLAlchemy. The primary purpose of Alkahest is to translate your database schema between different formats, helping to keep your documentation (DBML, Markdown) in sync with your actual database (SQL, SQLAlchemy). 

This project was born out of the need to maintain the AlembIQ database and keep its documentation synchronized. However, the functionality of Alkahest extends beyond this use case, as it can serve any project that requires similar work to be done.

## Features
- **Core Translation with the Translator Class**: The `Translator` class in `alkahest_functions.py` serves as the central hub for translating between Alkahest objects and their representations in DBML, SQL, and SQLAlchemy.
- **Python Classes for Database Components**: Alkahest provides a collection of Python classes representing database components such as `DataType`, `Column`, `Table`, and others.
- **Translation between PostgreSQL, SQLAlchemy, and DBML**: Alkahest can translate between these three representations of a database, assisting in keeping all representations synchronized.
- **Markdown Documentation Support**: Each Alkahest class has a `notes` attribute for storing Markdown documentation, allowing for in-line human-readable documentation that can be updated and accessed with ease.

## Project Structure
The Alkahest project is primarily built around the `Translator` class that facilitates the translation of database components. 

1. **translator.py**: Contains the `Translator` class and associated functions.
2. **classes.py**: Houses the Python classes that represent different components of a database, such as columns, tables, and schemas.
3. **dbml_lark.py**: Uses the Lark library to parse DBML strings into Alkahest objects.
4. **sql_sqlparse.py**: Uses the sqlparse library to parse SQL strings into Alkahest objects.

## Usage
Below is a quick guide on how to define a simple database schema using Alkahest and then translate it into DBML:

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

# Use the Translator class to convert this to DBML
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
For a detailed description of the Alkahest architecture and classes, please [visit the Wiki](https://github.com/calcanthum/alkahest/wiki).

## Feedback and Contributions
Alkahest is an ongoing project and is continuously evolving. Feedback, suggestions, and contributions are always welcome. To provide feedback, please raise an issue on GitHub.

## Why "Alkahest"?
The name is derived from an alchemical universal solvent, having the power to dissolve every other substance, including gold. Alkahest represents the ability to dissolve the barriers between different representations of a database schema — DBML, SQL, SQLAlchemy, and Markdown. Just as the mythical solvent was thought to be capable of reducing all compounds into their original elements, the Alkahest project reduces a database schema into its basic elements (tables, columns, relationships, etc.) and transforms them into different formats.

