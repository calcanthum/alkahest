from dbml_lark import dbml_parser
from alkahest_functions import Translator

# Mock DBML file path for testing
mock_dbml_file_path = "mock_dbml_file.dbml"

def test_dbml_to_alkahest_to_dbml():
    # Load the mock DBML schema
    with open(mock_dbml_file_path, "r") as file:
        original_dbml_schema = file.read()

    # Parse the DBML schema into Alkahest objects
    alkahest_schema = dbml_parser.parse(original_dbml_schema)

    # Translate the Alkahest objects back into a DBML schema
    translator = Translator(alkahest_schema)
    translated_dbml_schema = translator.to_dbml()

    # Compare the original DBML schema with the translated DBML schema
    assert original_dbml_schema == translated_dbml_schema, "Translation failed"