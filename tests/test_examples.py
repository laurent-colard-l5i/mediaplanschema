import os
import json
import pytest
import glob
from jsonschema import validate, RefResolver

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXAMPLES_PATH = os.path.join(BASE_DIR, "examples", "*.json")

example_files = glob.glob(EXAMPLES_PATH)

@pytest.mark.parametrize("example_file", example_files)
def test_example_is_valid(example_file):
    with open(example_file, "r", encoding="utf-8") as f:
        instance = json.load(f)

    # Get schema version from the example
    version = instance.get("meta", {}).get("schema_version")
    assert version is not None, f"No schema_version specified in meta block of {example_file}"

    schema_path = os.path.join(BASE_DIR, "schemas", version, "mediaplan.schema.json")
    assert os.path.exists(schema_path), f"Schema file not found for version: {version}"

    with open(schema_path, "r", encoding="utf-8") as sf:
        schema = json.load(sf)

    resolver = RefResolver(base_uri=f"file://{os.path.abspath(schema_path)}", referrer=schema)
    validate(instance=instance, schema=schema, resolver=resolver)
