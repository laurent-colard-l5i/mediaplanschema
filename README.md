# Media Plan Open Data Standard (mediaplanschema)

This repository defines a versioned, open, and extensible **JSON-based data standard** for representing media plans. It includes JSON Schema definitions, example media plans, and validation tooling for developers, analysts, and vendors working in the media planning ecosystem.

---

## Repository Structure

```
media-plan-ods/
├── schemas/             # Versioned JSON Schema definitions
│   ├── 0.0/
│   │   ├── campaign.schema.json
│   │   ├── lineitem.schema.json
│   │   └── mediaplan.schema.json
│   ├── 1.0/
│   │   ├── campaign.schema.json
│   │   ├── lineitem.schema.json
│   │   └── mediaplan.schema.json
│   └── schema_versions.json
├── examples/            # Example media plan files
│   ├── example_mediaplan_v0.0.json
│   └── example_mediaplan_v1.0.json
├── tests/               # Unit tests for schema validation
│   └── test_examples.py
├── .venv/               # Local Python virtual environment (not tracked in Git)
├── .gitignore
├── requirements.txt     # Python dependencies
└── README.md
```

---

## JSON Schema Overview

Schemas are versioned under `schemas/<major>.<minor>/`. The main schema file is:

```
schemas/1.0/mediaplan.schema.json
```

This references:
- `campaign.schema.json`
- `lineitem.schema.json`

Each media plan JSON file must include a `meta.schema_version` field that declares the schema version used (e.g., "1.0").

### Schema Versioning Strategy

**Major Version (X.0):** Breaking changes including renaming/removing fields, changing data types, changing allowable values, or adding required fields.

**Minor Version (X.Y):** Non-breaking changes including adding optional fields or adding new allowable values to existing fields.

Currently supported versions:
- **0.0**: Legacy schema with simpler structure
- **1.0**: Current schema with extended fields and structure

---

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/laurent-colard-l5i/mediaplanschema.git
cd mediaplanschema
```

### 2. Set Up a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate      # Mac/Linux
.venv\Scripts\activate.bat   # Windows (CMD)
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running Validation Tests

Run the unit test to validate all media plans in the `examples/` folder:

```bash
pytest tests/test_examples.py
```

Each example is dynamically validated against the appropriate schema version declared in its `meta.schema_version`.

---

## Adding a New Schema Version

To add a new schema version:

1. Duplicate an existing folder under `/schemas/` (e.g. `1.0` → `1.1`)
2. Modify schemas as needed
3. Update `schemas/schema_versions.json` to include the new version
4. Create new examples under `/examples/` with `"schema_version": "1.1"`
5. Re-run tests to validate

Example of updating `schema_versions.json`:
```json
{
  "current": "1.1",
  "supported": ["0.0", "1.0", "1.1"],
  "deprecated": [],
  "description": "Defines supported schema versions for media plans"
}
```

---

## Contributing

We welcome issues, schema proposals, and example files.

- Ensure you include `schema_version` in any proposed media plan examples
- All PRs are tested for schema validity via unit tests
- Contributions should follow semantic versioning when modifying schemas

---

## License

This project is open source under the [MIT License](LICENSE).

---

## Contact

Created and maintained by [Laurent Colard](https://github.com/laurent-colard-l5i).