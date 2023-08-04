
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

# Disclaimer
**AI-Assisted Parametric Development and Contributions**

This repository and its associated projects have been developed with the assistance of artificial intelligence (AI) models. Depending on the project, this may include one or more models such as GPT-like models, BART-like models, and other specialized transformer models. As a Parametric Developer, I have utilized these AI models to assist in writing, debugging, and documenting the code in this repository.

1. **AI Assistance**: AI models, while powerful and versatile, operate based on patterns and associations present in the data used for training. They have been instrumental in expediting the development process and providing insights. However, their outputs have been carefully reviewed and validated to ensure correctness, security, and efficiency.

2. **Accountability**: I have overseen the entire development process, including operating the IDE, managing the GitHub repositories, engineering prompts, designing the schema and architecture, and documenting the process. While AI plays a significant role, I take full responsibility for the outcomes of AI-assisted code generation and development, and I recognize the importance of maintaining the quality and integrity of the final codebase.

3. **Limitations**: AI models have inherent limitations. They lack the true understanding, context, and domain-specific knowledge that human developers possess. Therefore, any code or results produced by AI have been subject to rigorous testing, debugging, and validation before being included in the project.

4. **Collaborative Development**: I value collaboration, feedback, and constructive criticism from the developer community. While AI can streamline certain aspects of development, human expertise remains essential for complex problem-solving, architectural decisions, and ensuring the overall success of the project.

5. **Contributions**: Contributions from the developer community are welcome and appreciated. If you wish to contribute, please create a fork of the repository, make your changes, and submit a pull request. All contributions will be reviewed before being merged to ensure they align with the project's goals and standards.

6. **Acknowledgement**: The code in this repository is the result of a collaborative effort between AI models and potentially multiple human contributors. I appreciate the collaborative nature of open-source development and acknowledge the potential diversity of inputs in this project.

7. **Licensing**: This repository and associated projects are shared under [AGPL-3.0](LICENSE), which governs the usage, modification, and distribution of the code. Users and contributors are required to comply with the terms and conditions specified in the license.

In summary, this project employs AI models to enhance software development and documentation automation efforts. While AI plays a significant role, it is not a substitute for human expertise, and I am committed to maintaining the highest standards of code quality, security, and reliability through collaborative development and continuous improvement.

[Ivan Sabljak](https://github.com/calcanthum)