# MITRE ATT&CK Framework Mapping

This document maps Entra ID security findings to MITRE ATT&CK techniques.

## Overview

The MITRE ATT&CK framework is a comprehensive, adversary-focused taxonomy of attacker techniques based on real-world observations. This analyzer detects weaknesses that attackers exploit to achieve ATT&CK objectives.

---

## 1. Inactive Users → T1078 (Valid Accounts)

**MITRE Technique:** T1078 - Valid Accounts  
**Description:** Adversaries obtain and abuse credentials of existing accounts

**Attack Path:**
```
Inactive User (weak governance)
    ↓
Compromised credential exposure
    ↓
Lateral movement
    ↓
Persistence in environment
```

**How Our Check Helps:**
- Identifies accounts that are forgotten/unmonitored
- These accounts are attractive targets for credential reuse
- Disabling unused accounts reduces attack surface

**Mitigations:**
- MFA (T1078.004)
- Password policies (T1078.001)
- Account access controls

---

## 2. Orphaned Applications → T1547 (Boot or Logon Autostart Execution)

**MITRE Technique:** T1547 - Boot or Logon Autostart Execution  
**Description:** Adversaries configure system components or software to automatically execute during startup

**Attack Path:**
```
Orphaned App (no oversight)
    ↓
Attacker compromises app credentials
    ↓
Malicious scripts execute automatically
    ↓
Persistent backdoor established
```

**How Our Check Helps:**
- Identifies forgotten applications with standing access
- Reduces surface area for credential theft
- Ensures all active apps are actively managed

**Mitigations:**
- Application whitelisting
- Code review processes
- Privilege access management

---

## 3. Unused Service Principals → T1021 (Remote Services)

**MITRE Technique:** T1021 - Remote Services  
**Description:** Attackers use valid accounts to access resources via remote services

**Attack Path:**
```
Unused Service Principal (weak governance)
    ↓
Attacker discovers SP credentials in logs/artifacts
    ↓
Authenticates as service principal
    ↓
Lateral movement to connected systems
```

**How Our Check Helps:**
- Removes unused credentials from environment
- Reduces attack surface for lateral movement
- Enforces just-in-time credential management

**Mitigations:**
- Conditional access policies
- Multi-factor authentication
- Credential access controls

---

## 4. Weak MFA Configuration → T1556 (Modify Authentication Process)

**MITRE Technique:** T1556 - Modify Authentication Process  
**Description:** Adversaries modify authentication processes to bypass security controls

**Attack Path:**
```
No Passwordless Auth (weak MFA)
    ↓
Attacker performs phishing attack
    ↓
Obtains user password
    ↓
Bypasses weak MFA (SMS, email)
    ↓
Account compromise
```

**How Our Check Helps:**
- Flags weak authentication methods
- Encourages adoption of phishing-resistant MFA
- Windows Hello, FIDO2 prevent token-based attacks

**Mitigations:**
- Passwordless sign-in (Windows Hello, FIDO2)
- Push notification approval (prevents phishing)
- Hardware security keys

---

## 5. No Conditional Access → T1087 (Account Discovery)

**MITRE Technique:** T1087 - Account Discovery  
**Description:** Attackers enumerate user accounts and their roles

**Attack Path:**
```
No Conditional Access Policies
    ↓
Attacker accesses app from unusual location
    ↓
No risk-based authentication checks
    ↓
Attacker assumes compromised account
    ↓
Lateral movement to admin systems
```

**How Our Check Helps:**
- Detects absence of zero-trust access controls
- Conditional Access enforces risk-based authentication
- Blocks impossible travel, anomalous locations, non-compliant devices

**Mitigations:**
- Device compliance checks
- Location-based access controls
- Risky sign-in detection
- Real-time user/entity behavior analysis (UEBA)

---

## MITRE ATT&CK Tactics Covered

| Tactic | Technique | Check | Status |
|--------|-----------|-------|--------|
| **Initial Access** | T1199 (Trusted Relationship) | Orphaned Apps | ✅ |
| **Execution** | T1547 (Boot/Logon Autostart) | Orphaned Apps | ✅ |
| **Persistence** | T1547 (Autostart) | Orphaned Apps | ✅ |
| **Defense Evasion** | T1556 (Modify Auth) | Weak MFA | ✅ |
| **Lateral Movement** | T1021 (Remote Services) | Unused SPs | ✅ |
| **Discovery** | T1087 (Account Discovery) | No CA Policies | ✅ |
| **Credential Access** | T1110 (Brute Force) | Weak MFA | ✅ |

---

## ATT&CK Navigator Example

A visual representation of our coverage:

```
[Initial Access] ← Trusts weak governance
[Execution] ← Unused apps can execute
[Persistence] ← Orphaned apps establish persistence
[Defense Evasion] ← Weak MFA enables bypass
[Lateral Movement] ← Stolen SPs access other systems
[Discovery] ← No CA means no detection
[Credential Access] ← Phishing succeeds without MFA
```

---

## Future Coverage

These checks are not yet implemented:

- **T1098** (Account Manipulation) — Detecting unauthorized permission changes
- **T1123** (Audio Capture) — Detecting unauthorized app permissions
- **T1111** (Multi-Stage Channels) — Detecting unusual authentication methods
- **T1621** (Multi-Factor Authentication Interception) — Detecting MFA prompt bombing

---

## Using This Mapping

1. **For Security Assessments:** Map findings to MITRE techniques
2. **For Threat Modeling:** Understand attack paths enabled by findings
3. **For Compliance:** Demonstrate coverage against known techniques
4. **For Training:** Show how vulnerabilities enable real-world attacks
