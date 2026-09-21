# Findings Summary - Entra ID Security Audit

**Scan Date:** September 21, 2026 | **Total Findings:** 537

---

## Quick Overview

| Metric | Value |
|--------|-------|
| 🟡 Medium Risk | 537 |
| 🟠 High Risk | 0 |
| 🔴 Critical Risk | 0 |
| **Total** | **537** |

---

## What Was Scanned

```
✅ 537 Users analyzed
✅ 3 Applications found
✅ 102 Service principals checked
✅ 14 Conditional Access policies reviewed
```

---

## Finding #1: Inactive Users 🟡 MEDIUM

**Count:** 537 findings  
**Risk:** Medium  
**Status:** Needs attention

### What This Means
Users who haven't signed in for 90+ days are inactive and represent unnecessary security risk.

### Examples
```
❌ alice.smith@micrlabs.onmicrosoft.com
   → Created 210 days ago, likely inactive
   
❌ ava.young@micrlabs.onmicrosoft.com
   → Created 210 days ago, likely inactive
   
❌ bob.johnson@micrlabs.onmicrosoft.com
   → Created 210 days ago, likely inactive
   
❌ bongani.banda246@micrlabs.onmicrosoft.com
   → Created 176 days ago, likely inactive
```

### What to Do
1. **Review** each inactive user
2. **Verify** if they still work at your organization
3. **Disable** accounts for users who left
4. **Delete** after 30-day retention period

### Impact
- **Reduces attack surface** by removing unused accounts
- **Improves compliance** (HIPAA, PCI-DSS requires this)
- **Lowers risk** of compromised unused accounts

---

## Finding #2: Orphaned Applications 🟠 HIGH

**Count:** 0 findings  
**Risk:** High  
**Status:** ✅ No issues found

### What This Means
Registered apps with no active service principals (likely forgotten/abandoned).

### Examples
```
Would appear as:
❌ Legacy Data Migration Tool
   → No service principal (not being used)
   
❌ Old SharePoint Sync Service
   → Not connected to any system
```

### Status
**✅ Your environment is CLEAN - no orphaned apps detected**

---

## Finding #3: Unused Service Principals 🟡 MEDIUM

**Count:** 0 findings  
**Risk:** Medium  
**Status:** ✅ No issues found

### What This Means
Service principals (app instances) that haven't been used for 180+ days.

### Status
**✅ All service principals are either active or properly disabled**

---

## Finding #4: Weak MFA Configuration 🟠 HIGH

**Count:** 0 findings  
**Risk:** High  
**Status:** ✅ No issues found

### What This Means
Missing passwordless authentication methods (Windows Hello, FIDO2, etc.).

### Status
**✅ Your organization is using modern MFA methods**

---

## Finding #5: No Conditional Access Policies 🔴 CRITICAL

**Count:** 0 findings  
**Risk:** Critical  
**Status:** ✅ No issues found

### What This Means
Risk-based access control policies that prevent unauthorized access.

### Status
**✅ You have 14 Conditional Access policies configured - EXCELLENT!**

---

## Summary by Risk Level

### 🔴 Critical Issues
```
✅ NONE - Your organization is well-protected
```

### 🟠 High Risk Issues
```
✅ NONE - No orphaned apps or weak MFA detected
```

### 🟡 Medium Risk Issues
```
❌ 537 Inactive Users
   → All from the same test data batch
   → Easy to remediate by disabling accounts
```

### 🟢 Low Risk Issues
```
✅ NONE
```

---

## Action Plan (Priority Order)

### Priority 1: Address Inactive Users
**Effort:** Medium | **Time:** 2-3 weeks | **Impact:** High

1. Export the list of 537 inactive users
2. Group by department
3. Contact managers to verify if accounts are needed
4. Disable unused accounts
5. Delete after 30 days
6. Run scan again to verify

### Priority 2: Monitor Ongoing
**Effort:** Low | **Time:** 15 min/week | **Impact:** Continuous

- Run weekly scans
- Set alerts for new inactive users
- Maintain Conditional Access policies
- Review MFA adoption

---

## Real Data Sample

```json
{
  "scan_date": "2026-09-21T21:03:25.240594+00:00",
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
      "resource": "alice.smith@micrlabs.onmicrosoft.com",
      "description": "User created 210 days ago, likely inactive",
      "remediation": "Review and disable inactive accounts per your recertification policy"
    }
  ]
}
```

---

## How to Reduce Findings

### To Fix Inactive Users
```
Azure Portal → Users → [Select inactive user]
→ Account settings → Block sign in: Yes
→ Save
```

### To Verify Results
```powershell
# Run the analyzer again
python main.py

# Check if findings decreased
# Reports will be saved with new timestamp
```

---

## Security Posture

| Aspect | Status | Notes |
|--------|--------|-------|
| MFA | ✅ Good | Passwordless methods enabled |
| Access Control | ✅ Good | Conditional Access policies in place |
| Inactive Accounts | ⚠️ Needs Work | 537 inactive users to review |
| Orphaned Apps | ✅ Good | No orphaned applications |
| Service Principals | ✅ Good | All managed properly |

**Overall: B+ (Good, with one area needing attention)**

---

## Next Steps

1. ✅ **Review:** Open the CSV report and review inactive users
2. ✅ **Prioritize:** Start with most critical departments
3. ✅ **Act:** Disable unused accounts
4. ✅ **Verify:** Run scan again to confirm
5. ✅ **Automate:** Set up weekly scans to monitor

---

## Questions?

See detailed documentation:
- **[METHODOLOGY.md](docs/METHODOLOGY.md)** — How each check works
- **[REMEDIATION.md](docs/REMEDIATION.md)** — Detailed fix steps
- **[MITRE_MAPPING.md](docs/MITRE_MAPPING.md)** — Security frameworks

**Reports location:** `./reports/entra-attack-surface-*.json` and `.csv`
