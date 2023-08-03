class Translator:
    def __init__(self, obj):
        self.obj = obj

    def to_dbml(self):
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
            tables_dbml = "\n".join(self.to_dbml(table) for table in self.obj.tables.values())
            return f'Schema "{self.obj.name}" {{\n{tables_dbml}\n}}'
        elif isinstance(self.obj, Database):
            schemas_dbml = "\n".join(self.to_dbml(schema) for schema in self.obj.schemas.values())
            return f'Database "{self.obj.name}" {{\n{schemas_dbml}\n}}'
        else:
            raise TypeError("Unsupported type for translation")

    def to_sqlalchemy(self):
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
            tables_sqlalchemy = "\n".join(self.to_sqlalchemy(table) for table in self.obj.tables.values())
            return tables_sqlalchemy
        elif isinstance(self.obj, Database):
            schemas_sqlalchemy = "\n".join(self.to_sqlalchemy(schema) for schema in self.obj.schemas.values())
            return schemas_sqlalchemy
        else:
            raise TypeError("Unsupported type for translation")

    def to_sql(self):
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
            tables_sql = "\n".join(self.to_sql(table) for table in self.obj.tables.values())
            return tables_sql
        elif isinstance(self.obj, Database):
            schemas_sql = "\n".join(self.to_sql(schema) for schema in self.obj.schemas.values())
            return schemas_sql
        else:
            raise TypeError("Unsupported type for translation")
