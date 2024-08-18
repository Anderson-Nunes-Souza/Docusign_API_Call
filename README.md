# Docusign Integration Scripts

This repository contains scripts to facilitate the integration with Docusign for creating tokens and sending envelopes. Below is a description of each script and its usage.

## Scripts

### 1. `createToken.py`

**Description**: This script generates the token URL required for Docusign integration. The token is essential for authenticating API requests to Docusign.

**Usage**:
1. Ensure you have the necessary dependencies installed.
2. Run the script to generate the token URL.
3. Use the generated token in your API requests to authenticate.

```bash
python createToken.py
```

### 2. `envelopes_request.py`

**Description**: This script sends a POST request to create an envelope in Docusign. Envelopes are the core object within Docusign, representing the documents that need to be signed.

**Usage**:
1. Ensure you have the necessary dependencies installed.
2. Ensure you have a valid token (generated from `createToken.py`).
3. Run the script to create an envelope in Docusign.

```bash
python envelopes_request.py
```

## Prerequisites

- Python 3.x
- Necessary Python libraries (requests, json, etc.)
- Docusign account credentials and appropriate API keys

## Installation

1. Clone the repository:

```bash
git clone https://github.com/Anderson-Nunes-Souza/Docusign_API_Call.git
cd docusign-integration-scripts
```

## Configuration

Before running the scripts, ensure you have configured the necessary credentials and settings. You may need to update certain variables within the scripts to match your Docusign account details and API keys.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to adjust the repository URL, dependencies, and other details to match your specific setup and requirements.
