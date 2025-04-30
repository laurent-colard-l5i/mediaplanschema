import os
import json
import pytest
import glob
from jsonschema import validate, RefResolver

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXAMPLES_PATH = os.path.join(BASE_DIR, "examples", "*.json")
SCHEMA_REGISTRY_PATH = os.path.join(BASE_DIR, "schemas", "schema_versions.json")

# Load supported schema versions
with open(SCHEMA_REGISTRY_PATH, "r", encoding="utf-8") as vr:
    version_info = json.load(vr)
    supported_versions = version_info.get("supported", [])
    deprecated_versions = version_info.get("deprecated", [])
    current_version = version_info.get("current")

example_files = glob.glob(EXAMPLES_PATH)

@pytest.mark.parametrize("example_file", example_files)
def test_example_is_valid(example_file):
    with open(example_file, "r", encoding="utf-8") as f:
        instance = json.load(f)

    # Ensure schema version is declared
    version = instance.get("meta", {}).get("schema_version")
    assert version is not None, f"No schema_version specified in meta block of {example_file}"

    # Validate schema version against registry
    assert version in supported_versions, (
        f"Schema version '{version}' is not supported "
        f"(allowed: {supported_versions}) in file {example_file}"
    )

    # Load and validate against correct schema
    schema_path = os.path.join(BASE_DIR, "schemas", version, "mediaplan.schema.json")
    assert os.path.exists(schema_path), f"Schema file not found for version: {version}"

    with open(schema_path, "r", encoding="utf-8") as sf:
        schema = json.load(sf)

    resolver = RefResolver(base_uri=f"file://{os.path.abspath(schema_path)}", referrer=schema)
    validate(instance=instance, schema=schema, resolver=resolver)
