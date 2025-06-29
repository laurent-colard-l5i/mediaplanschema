# Media Plan Open Data Standard (mediaplanschema)

This repository defines a versioned, open, and extensible **JSON-based data standard** for representing media plans. It includes JSON Schema definitions, example media plans, and validation tooling for developers, analysts, and vendors working in the media planning ecosystem.

For developers looking to build applications with this standard, check out our **[mediaplanpy](https://github.com/laurent-colard-l5i/mediaplanpy)** sister repository - an open source Python SDK that provides the foundational tools you need to build, manage, and analyze media plans based on this Open Data Standard.

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
│   ├── 2.0/             # Current version
│   │   ├── campaign.schema.json
│   │   ├── dictionary.schema.json
│   │   ├── lineitem.schema.json
│   │   └── mediaplan.schema.json
│   └── schema_versions.json
├── examples/            # Example media plan files
│   ├── example_mediaplan_v0.0.json
│   ├── example_mediaplan_v1.0.json
│   └── example_mediaplan_v2.0.json
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
schemas/2.0/mediaplan.schema.json
```

This references:
- `campaign.schema.json`
- `lineitem.schema.json`
- `dictionary.schema.json`

### Version 2.0 (Current)

Version 2.0 introduces an additional schema file:
- `dictionary.schema.json` - Defines configuration for custom fields

The **dictionary schema** allows organizations to define custom dimensions, metrics, and cost fields with human-readable captions and descriptions. This enables standardized use of custom fields across different media planning tools and workflows while maintaining semantic meaning.

Each media plan JSON file must include a `meta.schema_version` field that declares the schema version used (e.g., "1.0" or "2.0").

### Schema Versioning Strategy

**Major Version (X.0):** Breaking changes including renaming/removing fields, changing data types, changing allowable values, or adding required fields.

**Minor Version (X.Y):** Non-breaking changes including adding optional fields or adding new allowable values to existing fields.

Currently supported versions:
- **0.0**: Deprecated - Legacy schema with simpler structure
- **1.0**: Supported - Stable schema with extended fields and structure
- **2.0**: Current - Enhanced version with custom field configuration via dictionary schema

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

Each example is dynamically validated against the appropriate schema version declared in its `meta.schema_version`. The test suite supports all versions including current and supported versions.

---

## Schema Version Details

### Version 0.0 (Deprecated)
- Basic structure with campaign and lineitem schemas
- Simple budget structure
- Limited customization options
- **Note**: This version is deprecated and should not be used for new implementations

### Version 1.0 (Supported)
- Enhanced campaign and lineitem schemas
- Expanded budget tracking with cost breakdowns
- Support for custom dimensions, metrics, and costs (up to 10 of each)
- Improved targeting and audience definition

### Version 2.0 (Current)
- All features from version 1.0
- **New dictionary schema** for custom field configuration
- Enhanced metadata tracking with separate creator ID and name fields
- Workflow status tracking
- Improved documentation and field descriptions
- Support for currency specification
- Additional standard metrics (engagements, followers, visits, leads, etc.)

#### Dictionary Schema Benefits (v2.0)
The dictionary schema enables:
- **Semantic clarity**: Define what each custom field represents
- **Tool interoperability**: Consistent field meanings across different platforms
- **Data governance**: Centralized configuration of custom field usage
- **User experience**: Human-readable captions for custom fields in applications

Example dictionary configuration:
```json
"dictionary": {
  "custom_dimensions": {
    "dim_custom1": {
      "status": "enabled",
      "caption": "Business Type",
      "description": "Classification of business model (B2B, B2C, B2B2C)"
    }
  }
}
```

---

## Developer Tools

### Python SDK - mediaplanpy

For developers building applications with this standard, we recommend using **[mediaplanpy](https://github.com/planmatic/mediaplanpy)** - our open source Python SDK that provides:

- **Schema validation** - Validate media plans against any schema version
- **Data manipulation** - Create, modify, and analyze media plan data
- **Import/Export** - Convert between different formats and systems
- **Analysis tools** - Built-in functions for media plan analysis and reporting

---

## Contributing

We welcome issues, schema proposals, and example files.

- Ensure you include `schema_version` in any proposed media plan examples
- All PRs are tested for schema validity via unit tests
- Contributions should follow semantic versioning when modifying schemas
- When proposing changes to current versions, consider backward compatibility impact

---

## License

This project is open source under the [MIT License](LICENSE).

---

## Contact

Created and maintained by [Planmatic.io](https://www.planmatic.io).