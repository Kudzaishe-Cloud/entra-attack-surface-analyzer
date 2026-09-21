# Entra ID Attack Surface Analyzer

**A production-ready Python tool for automated Entra ID security assessment and vulnerability discovery.**

![Badge](https://img.shields.io/badge/Python-3.11+-blue)
![Badge](https://img.shields.io/badge/License-MIT-green)

## Overview

This tool automatically discovers and documents security risks in your Azure Entra ID environment using the Microsoft Graph API. It identifies:

- ❌ Inactive user accounts
- 🔓 Orphaned applications with no service principals
- 🚫 Unused service principals (no sign-in activity)
- 🔐 Weak MFA configurations
- ⚠️ Missing Conditional Access policies

## Quick Start

### Prerequisites
- Python 3.11+
- Azure/Entra ID account with admin access
- Microsoft Graph API permissions

### Installation

```bash
git clone https://github.com/Kudzaishe-Cloud/entra-attack-surface-analyzer.git
cd entra-attack-surface-analyzer

python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### Configuration

Copy `.env.template` to `.env` and fill in your credentials:

```plaintext
TENANT_ID=your-tenant-id
CLIENT_ID=your-client-id
CLIENT_SECRET=your-client-secret
OUTPUT_DIR=./reports
```

**⚠️ WARNING:** Never commit `.env` to version control. It's already in `.gitignore`.

### Run Analysis

```bash
python main.py
```

Reports are generated in `./reports/` as JSON and CSV files.

## Features

✅ **Automated Discovery** — Scans all users, apps, service principals, and policies  
✅ **Risk Scoring** — Categorizes findings by severity (Critical, High, Medium, Low)  
✅ **Remediation Guidance** — Each finding includes actionable mitigation steps  
✅ **NIST CSF Aligned** — Checks map to NIST CSF controls  
✅ **GitHub Actions Ready** — Automated weekly scans  

## Documentation

- [METHODOLOGY.md](docs/METHODOLOGY.md) — How each check works and why it matters
- [REMEDIATION.md](docs/REMEDIATION.md) — Step-by-step fixes for common findings
- [MITRE_MAPPING.md](docs/MITRE_MAPPING.md) — How checks map to ATT&CK framework

## Tech Stack

- **Python 3.11** — Core language
- **Microsoft Graph API** — Entra ID data source
- **pytest** — Testing framework
- **GitHub Actions** — Scheduled scans

## Project Structure

```
entra-attack-surface-analyzer/
├── main.py                  # Entry point
├── requirements.txt         # Dependencies
├── .env.template           # Environment template
├── .gitignore              # Git ignore rules
├── modules/
│   ├── graph_client.py     # Microsoft Graph wrapper
│   ├── checks.py           # Vulnerability checks
│   └── reporters.py        # Report generation
├── docs/
│   ├── METHODOLOGY.md      # Check methodology
│   ├── REMEDIATION.md      # Fix instructions
│   └── MITRE_MAPPING.md    # ATT&CK mappings
└── reports/                # Generated reports (gitignored)
```

## License

MIT License — See LICENSE file

## Author

Kudzaishe Rutsinga  
GitHub: [@Kudzaishe-Cloud](https://github.com/Kudzaishe-Cloud)
