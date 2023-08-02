
class Entry:
    def __init__(self, dbml, sqlalchemy, sql):
        self.dbml = dbml
        self.sqlalchemy = sqlalchemy
        self.sql = sql

    def to_dbml(self):
        return self.dbml

    def to_sqlalchemy(self):
        return self.sqlalchemy

    def to_sql(self):
        return self.sql


class Table(Entry):
    def __init__(self, name, schema):
        dbml = f'Table "{schema}"."{name}"'
        sqlalchemy = f"Table('{name}', metadata, schema='{schema}')"
        sql = f"CREATE TABLE {schema}.{name}"
        super().__init__(dbml, sqlalchemy, sql)


class Column(Entry):
    def __init__(self, name, data_type):
        dbml = f'"{name}" {data_type}'
        sqlalchemy = f"Column('{name}', {data_type})"
        sql = f"{name} {data_type}"
        super().__init__(dbml, sqlalchemy, sql)


class NullableColumn(Column):
    def __init__(self, name, data_type):
        dbml = f'"{name}" {data_type} [optional]'
        sqlalchemy = f"Column('{name}', {data_type}, nullable=True)"
        sql = f"{name} {data_type} NULL"
        super().__init__(dbml, sqlalchemy, sql)


class DefaultColumn(Column):
    def __init__(self, name, data_type, default_value):
        dbml = f'"{name}" {data_type} [default: {default_value}]'
        sqlalchemy = f"Column('{name}', {data_type}, default={default_value})"
        sql = f"{name} {data_type} DEFAULT {default_value}"
        super().__init__(dbml, sqlalchemy, sql)


class PrimaryKeyColumn(Column):
    def __init__(self, name, data_type):
        dbml = f'"{name}" {data_type} [pk]'
        sqlalchemy = f"Column('{name}', {data_type}, primary_key=True)"
        sql = f"{name} {data_type} PRIMARY KEY"
        super().__init__(dbml, sqlalchemy, sql)


class ForeignKeyColumn(Column):
    def __init__(self, name, data_type, ref_table, ref_column):
        dbml = f'"{name}" {data_type} [ref: > "{ref_table}.{ref_column}"]'
        sqlalchemy = f"Column('{name}', {data_type}, ForeignKey('{ref_table}.{ref_column}'))"
        sql = f"{name} {data_type} REFERENCES {ref_table}({ref_column})"
        super().__init__(dbml, sqlalchemy, sql)


class CheckConstraint(Entry):
    def __init__(self, condition):
        dbml = "N/A"
        sqlalchemy = f"CheckConstraint('{condition}')"
        sql = f"CHECK ({condition})"
        super().__init__(dbml, sqlalchemy, sql)


dictionary = {
    "Table": Table,
    "Column": Column,
    "NullableColumn": NullableColumn,
    "DefaultColumn": DefaultColumn,
    "PrimaryKeyColumn": PrimaryKeyColumn,
    "ForeignKeyColumn": ForeignKeyColumn,
    "CheckConstraint": CheckConstraint
}

class DataType(Entry):
    def __init__(self, type_name):
        dbml = sqlalchemy = sql = type_name
        super().__init__(dbml, sqlalchemy, sql)


class Text(DataType):
    def __init__(self):
        super().__init__("text")


class Integer(DataType):
    def __init__(self):
        super().__init__("integer")


class Serial(DataType):
    def __init__(self):
        super().__init__("serial")


class Column(Entry):
    def __init__(self, name, data_type):
        dbml = f'"{name}" {data_type.to_dbml()}'
        sqlalchemy = f"Column('{name}', {data_type.to_sqlalchemy()})"
        sql = f"{name} {data_type.to_sql()}"
        super().__init__(dbml, sqlalchemy, sql)


dictionary.update({
    "DataType": DataType,
    "Text": Text,
    "Integer": Integer,
    "Serial": Serial
})
