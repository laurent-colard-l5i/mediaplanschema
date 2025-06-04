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

    # Load all schemas for this version
    schema_dir = os.path.join(BASE_DIR, "schemas", version)

    # Load main schema
    mediaplan_schema_path = os.path.join(schema_dir, "mediaplan.schema.json")
    assert os.path.exists(mediaplan_schema_path), f"Schema file not found for version: {version}"

    with open(mediaplan_schema_path, "r", encoding="utf-8") as sf:
        mediaplan_schema = json.load(sf)

    # Load campaign schema
    campaign_schema_path = os.path.join(schema_dir, "campaign.schema.json")
    with open(campaign_schema_path, "r", encoding="utf-8") as sf:
        campaign_schema = json.load(sf)

    # Load lineitem schema
    lineitem_schema_path = os.path.join(schema_dir, "lineitem.schema.json")
    with open(lineitem_schema_path, "r", encoding="utf-8") as sf:
        lineitem_schema = json.load(sf)

    # Create a custom resolver with all schemas preloaded
    schema_store = {
        "campaign.schema.json": campaign_schema,
        "lineitem.schema.json": lineitem_schema,
        "mediaplan.schema.json": mediaplan_schema
    }

    resolver = RefResolver(base_uri="", referrer=mediaplan_schema, store=schema_store)

    # Validate the instance
    validate(instance=instance, schema=mediaplan_schema, resolver=resolver)