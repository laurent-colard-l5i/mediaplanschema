import os
import json
import pytest
import glob
from jsonschema import validate, RefResolver

# Dynamically resolve absolute path to schema
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCHEMA_PATH = os.path.join(BASE_DIR, "schemas", "v1.0.0", "mediaplan.schema.json")
EXAMPLES_PATH = os.path.join(BASE_DIR, "examples", "*.json")

# Load schema
with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
    schema = json.load(f)

resolver = RefResolver(base_uri=f"file://{os.path.abspath(SCHEMA_PATH)}", referrer=schema)

example_files = glob.glob(EXAMPLES_PATH)

@pytest.mark.parametrize("example_file", example_files)
def test_example_is_valid(example_file):
    with open(example_file, "r", encoding="utf-8") as f:
        instance = json.load(f)
    validate(instance=instance, schema=schema, resolver=resolver)
