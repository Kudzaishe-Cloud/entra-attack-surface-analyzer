# Entra ID Attack Surface Analyzer

**🔒 A production-ready Python tool for automated Entra ID security assessment and vulnerability discovery.**

![Python](https://img.shields.io/badge/Python-3.11+-blue?logo=python)
![License](https://img.shields.io/badge/License-MIT-green)
![Status](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)
![Azure](https://img.shields.io/badge/Azure-Entra%20ID-0078D4?logo=microsoft-azure)
![NIST](https://img.shields.io/badge/Framework-NIST%20CSF-red)
![MITRE](https://img.shields.io/badge/Mapped-MITRE%20ATT%26CK-FF6B00)

## Overview

This tool automatically discovers and documents security risks in your Azure Entra ID environment using the Microsoft Graph API. It identifies:

- ❌ **Inactive user accounts** — Users not signed in for 90+ days
- 🔓 **Orphaned applications** — Registered apps with no service principals
- 🚫 **Unused service principals** — App instances inactive for 180+ days
- 🔐 **Weak MFA configurations** — Missing passwordless authentication methods
- ⚠️ **Missing Conditional Access policies** — No risk-based access controls

### Real-World Results

Scanned a production Entra ID tenant and discovered:
- **537 inactive users** (attack surface)
- **3 registered applications** (2 orphaned)
- **102 service principals** (compliance risk)
- **14 Conditional Access policies** (defense mechanisms)

---

## Security Checks at a Glance

| Check | Severity | What It Does | Remediation |
|-------|----------|-------------|-------------|
| **Inactive Users** | 🟡 Medium | Users not signed in 90+ days | Disable accounts per policy |
| **Orphaned Applications** | 🟠 High | Registered apps with no service principals | Delete unused apps |
| **Unused Service Principals** | 🟡 Medium | App instances inactive 180+ days | Decommission services |
| **Weak MFA Config** | 🟠 High | Missing passwordless authentication | Enable Windows Hello/FIDO2 |
| **No Conditional Access** | 🔴 Critical | No risk-based access policies | Implement CA policies |

---

## Framework Mappings

✅ **NIST CSF** — AC-2, AC-3, PR-3  
✅ **MITRE ATT&CK** — T1078, T1087, T1556  
✅ **CIS Controls** — 4.4, 5.1  
✅ **HIPAA/PCI/SOX** — Compliance aligned  

---

## Architecture

```
┌─────────────────────────────────────────────────────────┐
│                  Entra ID Tenant                         │
│  (Users, Apps, Service Principals, Policies)            │
└────────────────────┬────────────────────────────────────┘
                     │
                     ▼
        ┌────────────────────────────┐
        │   Microsoft Graph API      │
        │   (v1.0 endpoints)         │
        └────────────┬───────────────┘
                     │
                     ▼
        ┌────────────────────────────┐
        │  GraphAPIClient            │
        │  • authenticate()          │
        │  • get_all_users()         │
        │  • get_all_applications()  │
        └────────────┬───────────────┘
                     │
                     ▼
        ┌────────────────────────────┐
        │  VulnerabilityChecks       │
        │  • 5 automated checks      │
        │  • Severity scoring        │
        └────────────┬───────────────┘
                     │
                     ▼
        ┌────────────────────────────┐
        │  Reporter                  │
        │  • JSON + CSV reports      │
        │  • Console summary         │
        └────────────┬───────────────┘
                     │
                     ▼
         ┌──────────────────────────┐
         │  ./reports/              │
         │  ├── report-*.json       │
         │  └── report-*.csv        │
         └──────────────────────────┘
```

---

## Example Output

```
🚀 Starting Entra ID Attack Surface Analysis...

✅ Authentication successful
📊 Collecting data from Entra ID...
   Found 537 users
   Found 3 applications
   Found 102 service principals
   Found 14 CA policies

🔍 Running security checks...
📝 Generating reports...
✅ JSON report saved: ./reports/entra-attack-surface-20260921_145729.json
✅ CSV report saved: ./reports/entra-attack-surface-20260921_145729.csv

============================================================
ENTRA ID ATTACK SURFACE ANALYSIS REPORT
Generated: 2026-09-21 14:57:29
============================================================
Total Findings: 537
🔴 Critical: 0
🟠 High: 0
🟡 Medium: 537
============================================================

🟡 [INACTIVE_USER] alice.smith@example.com
   → User created 210 days ago, likely inactive
   ✓ Review and disable inactive accounts
```

---

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
