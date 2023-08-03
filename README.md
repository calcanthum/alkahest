# Alkahest

Alkahest is a Python-based project designed to act as a universal translation layer between DBML (Database Markup Language), SQL, and SQLAlchemy. The primary purpose of Alkahest is to aid in maintaining the consistency and accuracy of your database schemas and their corresponding documentation. 

This project was born out of the need to keep the AlembIQ database and its documentation synchronized. However, the functionality of Alkahest extends beyond this use case, as it can serve any project that requires translation between these database schema formats.

The project consists of a set of custom Python classes representing the elements of a database schema, and a set of functions that translate these elements between DBML, SQL, and SQLAlchemy.

## Structure of the Project

1. **alkahest_classes.py**: This file contains the definitions of various classes representing the elements of a database schema, such as `DataType`, `ForeignKey`, `Column`, `Table`, `Enum`, `Schema`, and `Relationship`.

2. **alkahest_functions.py**: This file contains the definitions of the `Translator` class, which is responsible for translating objects of the classes defined in `alkahest_classes.py` into appropriate representations in DBML, SQL, and SQLAlchemy.

3. **dbml_to_alkahest.py**: This file contains functions to parse DBML strings into Alkahest objects (defined in "alkahest_classes.py"). The primary function, `dbml_to_alkahest`, translates a DBML schema into an Alkahest `Schema` object.

## Usage

Alkahest enables you to translate your database schema between different formats. This is particularly useful when you need to keep your documentation (DBML, markdown) in sync with your actual database (SQL, SQLAlchemy).

Please note that this project is still under development. Contributions and feedback are welcome.