import re
from alkahest_classes import DataType, Column, Table, Enum, Relationship

def parse_data_type(dbml_string):
    """Parse a DataType from a DBML string."""
    match = re.match(r'\b(\w+)\b', dbml_string)
    if match:
        data_type_dbml = match.group(1)
        data_type = DataType(dbml=data_type_dbml, sqlalchemy=data_type_dbml, sql=data_type_dbml)
        return data_type
    else:
        raise ValueError(f"Could not parse data type from string: {dbml_string}")

def parse_column(dbml_string):
    """Parse a Column from a DBML string."""
    dbml_string = dbml_string.strip()
    parts = dbml_string.split(' ', 1)
    if len(parts) < 2:
        raise ValueError(f"Could not parse column from string: {dbml_string}")
    
    column_name = parts[0]
    data_type = parse_data_type(parts[1])
    
    nullable = True
    primary_key = False
    default_value = None
    
    if '[' in parts[1] and ']' in parts[1]:
        settings = parts[1].split('[', 1)[1].split(']')[0].split(',')
        for setting in settings:
            setting = setting.strip()
            if setting == 'not null':
                nullable = False
            elif setting == 'pk':
                primary_key = True
            elif setting.startswith('default:'):
                default_value = setting.split(':')[1].strip()
    
    column = Column(name=column_name, data_type=data_type, nullable=nullable, primary_key=primary_key, default_value=default_value)
    return column

def parse_table(dbml_string):
    """Parse a Table from a DBML string."""
    dbml_string = dbml_string.strip()
    parts = dbml_string.split(' ', 1)
    if len(parts) < 2 or parts[0].lower() != 'table':
        raise ValueError(f"Could not parse table from string: {dbml_string}")
    
    parts = parts[1].split('{', 1)
    if len(parts) < 2:
        raise ValueError(f"Could not parse table from string: {dbml_string}")
    
    table_name = parts[0].strip()
    column_definitions = parts[1].strip('} ').split('\n')
    columns = {column_def.split(' ')[0]: parse_column(column_def) for column_def in column_definitions if column_def.strip()}
    
    table = Table(name=table_name, columns=columns)
    return table

def parse_enum(dbml_string):
    """Parse an Enum from a DBML string."""
    dbml_string = dbml_string.strip()
    parts = dbml_string.split(' ', 1)
    if len(parts) < 2 or parts[0].lower() != 'enum':
        raise ValueError(f"Could not parse enum from string: {dbml_string}")
    
    parts = parts[1].split('{', 1)
    if len(parts) < 2:
        raise ValueError(f"Could not parse enum from string: {dbml_string}")
    
    enum_name = parts[0].strip()
    values = [value.strip() for value in parts[1].strip('} ').split('\n') if value.strip()]
    
    enum = Enum(name=enum_name, values=values)
    return enum

def parse_relationships(tables):
    """Parse many-to-many relationships from a list of Tables."""
    relationships = []
    for table in tables:
        if all(column.foreign_key for column in table.columns.values()):
            # This is a junction table, extract the many-to-many relationship
            referenced_tables = [column.foreign_key.references.split('.')[0] for column in table.columns.values()]
            relationship = Relationship(tables=referenced_tables, through=table.name)
            relationships.append(relationship)
    return relationships
