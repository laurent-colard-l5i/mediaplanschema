# Media Plan Open Data Standard (ODS)

This repository defines a versioned, open, and extensible **JSON-based data standard** for representing media plans. It includes JSON Schema definitions, example media plans, and validation tooling for developers, analysts, and vendors working in the media planning ecosystem.

---

## Repository Structure

```
media-plan-ods/
├── schemas/             # Versioned JSON Schema definitions
│   └── v1.0.0/
│       ├── campaign.schema.json
│       ├── lineitem.schema.json
│       └── mediaplan.schema.json
├── examples/            # Example media plan files
│   └── mediaplan_example.json
├── tests/               # Unit tests for schema validation
│   └── test_examples.py
├── .venv/               # Local Python virtual environment (not tracked in Git)
├── .gitignore
├── requirements.txt     # Python dependencies
└── README.md
```

---

## JSON Schema Overview

Schemas are versioned under `schemas/v<version>/`. The main schema file is:

```
schemas/v1.0.0/mediaplan.schema.json
```

This references:
- `campaign.schema.json`
- `lineitem.schema.json`

Each media plan JSON file must include a `meta.schema_version` field that declares the schema version used.

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

1. Duplicate an existing folder under `/schemas/` (e.g. `v1.0.0` → `v1.1.0`)
2. Modify schemas as needed
3. Create new examples under `/examples/` with `"schema_version": "v1.1.0"`
4. Re-run tests to validate

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