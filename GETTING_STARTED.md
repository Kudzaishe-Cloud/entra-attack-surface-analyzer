# Getting Started: Complete Step-by-Step Guide

**A hands-on walkthrough to build and run your own Entra ID security scanner from scratch.**

---

## Part 1: Set Up Your Azure App (15 minutes)

### Step 1a: Open Azure Portal

1. Go to **https://portal.azure.com**
2. Sign in with your account
3. Search for **"App registrations"**

### Step 1b: Register Your Application

1. Click **"New registration"**
2. Fill in:
   - **Name:** `Entra-ID-Attack-Surface-Analyzer`
   - **Account types:** "Accounts in this organizational directory only"
3. Click **"Register"**
4. **SAVE these values:**
   - Application (client) ID
   - Directory (tenant) ID

### Step 1c: Create a Client Secret

1. Click **"Certificates & secrets"**
2. Click **"New client secret"**
3. Set:
   - **Description:** `analyzer-secret`
   - **Expires:** `24 months`
4. Click **"Add"**
5. **COPY THE VALUE IMMEDIATELY** (won't see it again!)

### Step 1d: Grant API Permissions

1. Click **"API permissions"**
2. Click **"Add a permission"**
3. Select **"Microsoft Graph"** → **"Application permissions"**
4. Add these 5 permissions:
   - `Directory.Read.All`
   - `Application.Read.All`
   - `ServicePrincipal.Read.All`
   - `AuditLog.Read.All`
   - `Policy.Read.All`
5. Click **"Grant admin consent for [Your Org]"**
6. Wait for **✅ checkmarks**

---

## Part 2: Download & Install (10 minutes)

### Step 2a: Open Terminal

**Windows:** Press `Win + R` → type `powershell` → Enter

### Step 2b: Create Project Folder

```powershell
mkdir C:\entra-analyzer
cd C:\entra-analyzer
```

### Step 2c: Download Tool

```powershell
git clone https://github.com/Kudzaishe-Cloud/entra-attack-surface-analyzer.git .
```

### Step 2d: Create Virtual Environment

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Step 2e: Install Dependencies

```powershell
pip install -r requirements.txt
```

---

## Part 3: Configure Credentials (5 minutes)

### Step 3a: Create .env File

```powershell
copy .env.template .env
notepad .env
```

### Step 3b: Edit .env

Add your values from Step 1:

```plaintext
TENANT_ID=<your-directory-id-from-step-1b>
CLIENT_ID=<your-app-id-from-step-1b>
CLIENT_SECRET=<your-secret-value-from-step-1c>
OUTPUT_DIR=./reports
```

Save the file.

---

## Part 4: Run Your First Scan (2 minutes)

```powershell
python main.py
```

You'll see:
```
🚀 Starting Entra ID Attack Surface Analysis...
✅ Authentication successful
📊 Collecting data...
Found 537 users, 3 apps, 102 service principals
🔍 Running checks...
📝 Generating reports...
✅ Complete!
```

---

## Part 5: Review Reports (5 minutes)

### View JSON Report

```powershell
cat .\reports\entra-attack-surface-*.json | python -m json.tool
```

### View CSV Report

Open in Excel:
```
File Explorer → reports → entra-attack-surface-*.csv → Open with Excel
```

---

## Part 6: Understand Findings (10 minutes)

### 🟡 INACTIVE_USER (Medium)
- User hasn't signed in for 90+ days
- **Action:** Review and disable if no longer needed

### 🟠 ORPHANED_APPLICATION (High)
- Registered app with no active service principal
- **Action:** Verify it's needed, delete if not

### 🟠 WEAK_MFA_CONFIG (High)
- No passwordless authentication configured
- **Action:** Enable Windows Hello or FIDO2

### 🔴 NO_CONDITIONAL_ACCESS (Critical)
- No Conditional Access policies
- **Action:** Implement risk-based access controls

---

## Part 7: Take Action

### Disable Inactive Users
1. Azure Portal → Users
2. Find user → Click → Account settings
3. Set "Enabled" to "No"
4. Save

### Delete Orphaned Apps
1. Azure Portal → App registrations
2. Find app → Click → Delete

### Enable MFA
1. Azure Portal → Multifactor authentication
2. Enable Windows Hello, FIDO2, Authenticator app

---

## Summary: What You Did

✅ Created Azure app with Graph API access  
✅ Installed the security scanner  
✅ Configured credentials  
✅ Ran your first scan  
✅ Found security findings  
✅ Reviewed reports  
✅ Took action to fix risks  

**Total: ~45 minutes**

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "Authentication failed" | Check credentials in .env file |
| "Module not found" | Run: `pip install -r requirements.txt` |
| ".env not found" | Run: `copy .env.template .env` |
| "venv not activated" | Run: `.\venv\Scripts\Activate.ps1` |

---

**Ready? Let's go! Follow [VISUAL_WALKTHROUGH.md](VISUAL_WALKTHROUGH.md) to see what you'll see.** 🚀
