
# Alkahest

Alkahest is a Python-based project designed to act as a universal translation layer between DBML (Database Markup Language), SQL, and SQLAlchemy. The primary purpose of Alkahest is to aid in maintaining the consistency and accuracy of your database schemas and their corresponding documentation. 

This project was born out of the need to keep the AlembIQ database and its documentation synchronized. However, the functionality of Alkahest extends beyond this use case, as it can serve any project that requires translation between these database schema formats.

## Project Structure

The project consists of a set of custom Python classes representing the elements of a database schema, a set of functions that translate these elements between DBML, SQL, and SQLAlchemy, and a parser that transforms DBML schemas into Alkahest objects.

1. **alkahest_classes.py**: This file contains the definitions of various classes that represent the different elements of a database schema. These include `Database`, `Schema`, `Table`, `Column`, `DataType`, `ForeignKey`, `Relationship`, and `View`.

2. **alkahest_functions.py**: This file contains the `Translator` class, which handles the translation of Alkahest objects (as defined in `alkahest_classes.py`) into their appropriate representations in DBML, SQL, and SQLAlchemy.

3. **dbml_lark.py**: This file uses the Lark library to parse DBML strings into Alkahest objects.

## Usage

Alkahest enables you to translate your database schema between different formats, helping to keep your documentation (DBML, Markdown) in sync with your actual database (SQL, SQLAlchemy). 

Additionally, Alkahest's capability to transform a database schema into a set of Python objects provides a platform for more advanced manipulations, such as schema modification, validation, and comparison.

## Documentation

For a detailed description of the Alkahest architecture and classes, please visit the Wiki.

## Feedback and Contributions

Alkahest is an ongoing project and is continuously evolving. Feedback, suggestions, and contributions are always welcome.

## Why "Alkahest"?

The name is derived from an alchemical universal solvent, having the power to dissolve every other substance, including gold.

Alkahest represents the ability to dissolve the barriers between different representations of a database schema — DBML, SQL, SQLAlchemy, and Markdown. Just as the mythical solvent was thought to be capable of reducing all compounds into their original elements, the Alkahest project reduces a database schema into its basic elements (tables, columns, relationships, etc.) and transforms them into different formats.
