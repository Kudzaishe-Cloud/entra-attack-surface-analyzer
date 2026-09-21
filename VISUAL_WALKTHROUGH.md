# Visual Walkthrough: See What You'll See

**This shows EXACTLY what appears when you follow the steps.**

---

## Section 1: Azure Portal Interface

### App Registrations Page

```
┌─────────────────────────────────────────────────┐
│  Azure Portal                              🔍   │
├─────────────────────────────────────────────────┤
│  App registrations                              │
│                                                 │
│  + New registration                             │
│                                                 │
│  Entra-ID-Attack-Surface-Analyzer   (You)       │
│  Microsoft Graph                     (MS)       │
└─────────────────────────────────────────────────┘
```

### After Registration

```
┌─────────────────────────────────────────────────┐
│  Application Overview                            │
├─────────────────────────────────────────────────┤
│                                                 │
│  Application (client) ID                        │
│  ┌───────────────────────────────────────────┐ │
│  │ [your-app-id-here]             [Copy]    │ │
│  └───────────────────────────────────────────┘ │
│                                                 │
│  Directory (tenant) ID                          │
│  ┌───────────────────────────────────────────┐ │
│  │ [your-tenant-id-here]          [Copy]    │ │
│  └───────────────────────────────────────────┘ │
│                                                 │
└─────────────────────────────────────────────────┘
```

### Client Secret Section

```
┌─────────────────────────────────────────────────┐
│  Certificates & secrets                         │
├─────────────────────────────────────────────────┤
│                                                 │
│  Client secrets                                 │
│  ┌───────────────────────────────────────────┐ │
│  │ analyzer-secret  9/21/26  9/21/28  Copy  │ │
│  └───────────────────────────────────────────┘ │
│                                                 │
│  Value (shown only once):                      │
│  ┌───────────────────────────────────────────┐ │
│  │ [your-secret-here]               [Copy] │ │
│  └───────────────────────────────────────────┘ │
│  👉 COPY IMMEDIATELY - you won't see it again  │
│                                                 │
└─────────────────────────────────────────────────┘
```

### API Permissions Page

```
┌─────────────────────────────────────────────────┐
│  API permissions                                 │
├─────────────────────────────────────────────────┤
│                                                 │
│  [+ Add permission]  [Grant admin consent]     │
│                                                 │
│  Configured permissions                         │
│  ✅ Directory.Read.All                          │
│  ✅ Application.Read.All                        │
│  ✅ ServicePrincipal.Read.All                   │
│  ✅ AuditLog.Read.All                           │
│  ✅ Policy.Read.All                             │
│                                                 │
│  👉 Green checkmarks = Ready!                   │
│                                                 │
└─────────────────────────────────────────────────┘
```

---

## Section 2: PowerShell Terminal

### Clone Repository

```powershell
PS C:\entra-analyzer> git clone https://github.com/...entra-attack-surface-analyzer.git .
Cloning into '.'...
remote: Enumerating objects: 100, done.
remote: Counting objects: 100% done.
remote: Receiving objects: 100% done.
Resolving deltas: 100% done.

PS C:\entra-analyzer>
```

### Create Virtual Environment

```powershell
PS C:\entra-analyzer> python -m venv venv
PS C:\entra-analyzer> .\venv\Scripts\Activate.ps1

(venv) PS C:\entra-analyzer>
     👉 Notice "(venv)" at the start = Active!
```

### Install Dependencies

```powershell
(venv) PS C:\entra-analyzer> pip install -r requirements.txt
Collecting msgraph-core==0.2.2
  Downloading msgraph_core-0.2.2-py3-none-any.whl
...
Successfully installed PyJWT-2.14.0 azure-core-1.41.0 ...

(venv) PS C:\entra-analyzer>
```

### Create .env File

```powershell
(venv) PS C:\entra-analyzer> copy .env.template .env
(venv) PS C:\entra-analyzer> notepad .env
     👉 Opens text editor - fill in your credentials
```

---

## Section 3: Running the Analyzer

### Console Output

```powershell
(venv) PS C:\entra-analyzer> python main.py

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

🟡 [INACTIVE_USER] bob.johnson@example.com
   → User created 210 days ago, likely inactive
   ✓ Review and disable inactive accounts

... (more findings)

(venv) PS C:\entra-analyzer>
     👉 SUCCESS! Scan complete!
```

---

## Section 4: Viewing Reports

### JSON Report (Pretty Printed)

```json
{
  "scan_date": "2026-09-21T14:57:29.123456+00:00",
  "total_findings": 537,
  "findings_by_severity": {
    "CRITICAL": 0,
    "HIGH": 0,
    "MEDIUM": 537,
    "LOW": 0
  },
  "findings": [
    {
      "type": "INACTIVE_USER",
      "severity": "MEDIUM",
      "resource": "alice.smith@example.com",
      "description": "User created 210 days ago, likely inactive",
      "remediation": "Review and disable inactive accounts"
    },
    {
      "type": "ORPHANED_APPLICATION",
      "severity": "HIGH",
      "resource": "Legacy Data Migration Tool",
      "description": "Registered app has no service principal",
      "remediation": "Verify app is needed; delete if orphaned"
    }
  ]
}
```

### CSV Report in Excel

```
┌────────────┬──────────────────────┬─────────────────────┬──────────────┐
│ severity   │ type                 │ resource            │ description  │
├────────────┼──────────────────────┼─────────────────────┼──────────────┤
│ MEDIUM     │ INACTIVE_USER        │ alice.smith@ex...   │ User created │
│ MEDIUM     │ INACTIVE_USER        │ bob.johnson@ex...   │ User created │
│ HIGH       │ ORPHANED_APPLICATION │ Legacy Data Mig...  │ Registered   │
│ HIGH       │ WEAK_MFA_CONFIG      │ Auth Policy         │ No password  │
│            │                      │                     │              │
└────────────┴──────────────────────┴─────────────────────┴──────────────┘
     👉 Open in Excel for filtering and sorting!
```

---

## Section 5: File Structure Created

```
C:\entra-analyzer\
├── venv/                    (Python environment)
│   ├── Scripts/
│   └── Lib/
│
├── modules/                 (Code)
│   ├── graph_client.py
│   ├── checks.py
│   └── reporters.py
│
├── reports/                 (Output - NEW!)
│   ├── entra-attack-surface-*.json
│   └── entra-attack-surface-*.csv
│
├── .env                     (Your credentials)
├── main.py                  (Entry point)
├── requirements.txt         (Dependencies)
└── README.md                (Documentation)
```

---

## Section 6: Taking Action in Azure

### Disabling a User

```
Azure Portal → Users → alice.smith → Account settings

┌─────────────────────────────────────┐
│ Block sign in                        │
│ ○ No                                 │
│ ● Yes  ← Click to disable            │
│                                       │
│              [Save]                  │
└─────────────────────────────────────┘
```

### Deleting an Orphaned App

```
Azure Portal → App registrations → [Select app] → Delete

┌─────────────────────────────────────┐
│ Are you sure?                        │
│                                     │
│ You are about to delete this app.   │
│                                     │
│        [Cancel]  [Delete]           │
└─────────────────────────────────────┘
```

---

## Summary Table

| Step | Action | What You See |
|------|--------|------------|
| 1 | Register app | App ID and Tenant ID appear |
| 2 | Create secret | Secret value (copy immediately!) |
| 3 | Grant permissions | 5 green checkmarks ✅ |
| 4 | Clone repo | Files downloaded |
| 5 | Create venv | "(venv)" in command prompt |
| 6 | Install deps | "Successfully installed..." |
| 7 | Create .env | File created with your credentials |
| 8 | Run analyzer | Real-time progress output |
| 9 | Check reports | JSON and CSV files created |
| 10 | Review findings | 537+ security issues displayed |
| 11 | Take action | Fix issues in Azure Portal |
| 12 | Verify | Re-run to confirm fixes |

---

**Ready to do it? Start with [GETTING_STARTED.md](GETTING_STARTED.md)** 🚀
