class Translator:
    """
    The Translator class provides methods to translate Alkahest objects into their respective representations
    in DBML, SQL, and SQLAlchemy.

    Attributes:
        obj (Object): The Alkahest object to be translated.
    """
    def __init__(self, obj):
        """
        Initializes a Translator object with the given Alkahest object.

        Args:
            obj (Object): The Alkahest object to be translated.
        """
        self.obj = obj

    def to_dbml(self):
        """
        Translates the Alkahest object into its DBML representation.

        Returns:
            str: The DBML representation of the Alkahest object.
        """
        if isinstance(self.obj, DataType):
            return self.obj.dbml
        elif isinstance(self.obj, Column):
            null_str = ' [not null]' if not self.obj.nullable else ''
            pk_str = ' [pk]' if self.obj.primary_key else ''
            fk_str = f' [ref: > {self.obj.foreign_key.table}.{self.obj.foreign_key.column}]' if self.obj.foreign_key else ''
            return f'"{self.obj.name}" {self.obj.data_type.dbml}{null_str}{pk_str}{fk_str}'
        elif isinstance(self.obj, Table):
            columns_dbml = "\n".join(self.to_dbml(column) for column in self.obj.columns.values())
            return f'Table "{self.obj.name}" {{\n{columns_dbml}\n}}'
        elif isinstance(self.obj, Schema):
            enums_dbml = "\n".join(self.to_dbml(enum) for enum in self.obj.enums.values())
            tables_dbml = "\n".join(self.to_dbml(table) for table in self.obj.tables.values())
            return f'Schema "{self.obj.name}" {{\n{enums_dbml}\n{tables_dbml}\n}}'
        elif isinstance(self.obj, Database):
            schemas_dbml = "\n".join(self.to_dbml(schema) for schema in self.obj.schemas.values())
            return f'Database "{self.obj.name}" {{\n{schemas_dbml}\n}}'
        elif isinstance(self.obj, View):
            return f'View "{self.obj.name}" As SQL\n{self.obj.sql}\nEnd'
        elif isinstance(self.obj, Enum):
            values_dbml = ", ".join(f'"{value}"' for value in self.obj.values)
            return f'Enum "{self.obj.name}" {{ {values_dbml} }}'
        else:
            raise TypeError("Unsupported type for translation")

    def to_sqlalchemy(self):
        """
        Translates the Alkahest object into its SQLAlchemy representation.

        Returns:
            str: The SQLAlchemy representation of the Alkahest object.
        """
        if isinstance(self.obj, DataType):
            return self.obj.sqlalchemy
        elif isinstance(self.obj, Column):
            null_str = ', nullable=False' if not self.obj.nullable else ''
            pk_str = ', primary_key=True' if self.obj.primary_key else ''
            fk_str = f', ForeignKey("{self.obj.foreign_key.table}.{self.obj.foreign_key.column}")' if self.obj.foreign_key else ''
            return f'{self.obj.name} = Column({self.obj.data_type.sqlalchemy}{null_str}{pk_str}{fk_str})'
        elif isinstance(self.obj, Table):
            columns_sqlalchemy = ",\n".join(self.to_sqlalchemy(column) for column in self.obj.columns.values())
            return f'class {self.obj.name}(Base):\n    __tablename__ = "{self.obj.name}"\n{columns_sqlalchemy}'
        elif isinstance(self.obj, Schema):
            enums_sqlalchemy = "\n".join(self.to_sqlalchemy(enum) for enum in self.obj.enums.values())
            tables_sqlalchemy = "\n".join(self.to_sqlalchemy(table) for table in self.obj.tables.values())
            return f'{enums_sqlalchemy}\n{tables_sqlalchemy}'
        elif isinstance(self.obj, Database):
            schemas_sqlalchemy = "\n".join(self.to_sqlalchemy(schema) for schema in self.obj.schemas.values())
            return f'{schemas_sqlalchemy}'
        elif isinstance(self.obj, View):
            return f'# No SQLAlchemy equivalent for View. Consider creating a SQLAlchemy select statement for "{self.obj.name}" view instead.'
        elif isinstance(self.obj, Enum):
            values_sqlalchemy = ", ".join(f'"{value}"' for value in self.obj.values)
            return f'{self.obj.name} = Enum({values_sqlalchemy})'
        else:
            raise TypeError("Unsupported type for translation")

    def to_sql(self):
        """
        Translates the Alkahest object into its SQL representation.

        Returns:
            str: The SQL representation of the Alkahest object.
        """
        if isinstance(self.obj, DataType):
            return self.obj.sql
        elif isinstance(self.obj, Column):
            null_str = ' NOT NULL' if not self.obj.nullable else ''
            pk_str = ' PRIMARY KEY' if self.obj.primary_key else ''
            fk_str = f' REFERENCES {self.obj.foreign_key.table}({self.obj.foreign_key.column})' if self.obj.foreign_key else ''
            return f'"{self.obj.name}" {self.obj.data_type.sql}{null_str}{pk_str}{fk_str}'
        elif isinstance(self.obj, Table):
            columns_sql = ",\n".join(self.to_sql(column) for column in self.obj.columns.values())
            return f'CREATE TABLE "{self.obj.name}" (\n{columns_sql}\n);'
        elif isinstance(self.obj, Schema):
            enums_sql = "\n".join(self.to_sql(enum) for enum in self.obj.enums.values())
            tables_sql = "\n".join(self.to_sql(table) for table in self.obj.tables.values())
            return f'{enums_sql}\n{tables_sql}'
        elif isinstance(self.obj, Database):
            schemas_sql = "\n".join(self.to_sql(schema) for schema in self.obj.schemas.values())
            return f'{schemas_sql}'
        elif isinstance(self.obj, View):
            return self.obj.sql
        elif isinstance(self.obj, Enum):
            values_sql = ", ".join(f"'{value}'" for value in self.obj.values)
            return f'CREATE TYPE {self.obj.name} AS ENUM ({values_sql});'
        else:
            raise TypeError("Unsupported type for translation")
