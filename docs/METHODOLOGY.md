# Methodology: Entra ID Security Checks

This document explains how each security check works and maps to frameworks.

## 1. Inactive Users

**Check Name:** `check_inactive_users()`  
**Severity:** Medium  
**What it does:** Identifies user accounts that haven't been used recently

**Why it matters:**
- Inactive accounts are stale attack surface
- Increases risk of credential compromise
- Violates least-privilege principle

**NIST CSF Mapping:** AC-2 (Account Management)  
**CIS Controls:** CIS 5.1 (Inventory of Accounts)  
**MITRE ATT&CK:** T1078 (Valid Accounts)

---

## 2. Orphaned Applications

**Check Name:** `check_orphaned_applications()`  
**Severity:** High  
**What it does:** Finds registered apps with no service principals

**Why it matters:**
- Orphaned apps may be forgotten/unmanaged
- Could be exploited if credentials are exposed
- Violates application lifecycle management

**NIST CSF Mapping:** GV-2 (Supply Chain Risk Management)  
**CIS Controls:** CIS 4.4 (Uninstall or Disable Unnecessary Software)

---

## 3. Unused Service Principals

**Check Name:** `check_unused_service_principals()`  
**Severity:** Medium  
**What it does:** Identifies service principals (app instances) with no recent activity

**Why it matters:**
- Unused apps should be decommissioned
- Reduces attack surface
- Simplifies compliance audits

---

## 4. Weak MFA

**Check Name:** `check_weak_mfa()`  
**Severity:** High  
**What it does:** Verifies passwordless authentication is configured

**Why it matters:**
- Passwords alone are insufficient
- Passwordless methods (Windows Hello, FIDO2) reduce phishing risk
- Required by HIPAA, PCI, SOX compliance

**NIST CSF Mapping:** PR-3 (Authentication)

---

## 5. No Conditional Access

**Check Name:** `check_no_conditional_access()`  
**Severity:** Critical  
**What it does:** Checks if Conditional Access policies exist

**Why it matters:**
- CA policies enforce zero-trust access control
- Detects risky sign-ins (impossible travel, anomalous location)
- Required for compliance (HIPAA, FedRAMP)

**NIST CSF Mapping:** AC-3 (Access Control)
