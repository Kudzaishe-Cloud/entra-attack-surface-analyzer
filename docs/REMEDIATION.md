# Remediation Guide: Fixing Entra ID Security Findings

This guide provides step-by-step instructions for remediating each finding type.

## Inactive Users

### Steps to Remediate

1. **Identify Inactive Users**
   - Review the analysis report for users in "INACTIVE_USER" findings
   - Check last sign-in date and usage patterns

2. **Verify Necessity**
   - Contact department manager to confirm if account is still needed
   - Check for active projects, group memberships, resource access

3. **Disable Account** (if not needed)
   ```
   Azure Portal → Users → Select inactive user → Account settings → Enabled: No
   ```

4. **Delete Account** (if confirmed unnecessary)
   ```
   Azure Portal → Users → Select user → Delete
   ```

5. **Document Action**
   - Log in change management system (ServiceNow, etc.)
   - Update access review records

### Timeline
- **Phase 1:** Identify and notify users (1 week)
- **Phase 2:** Disable active unused accounts (1 week)
- **Phase 3:** Delete accounts after retention period (30 days)

---

## Orphaned Applications

### Steps to Remediate

1. **Identify Orphaned Apps**
   - Review "ORPHANED_APPLICATION" findings
   - List all registered apps with no service principals

2. **Verify App Purpose**
   - Check app's owner in Entra ID registration
   - Search code repositories for references
   - Query Azure DevOps/GitHub for CI/CD pipelines using the app

3. **Delete Orphaned App**
   ```
   Azure Portal → App registrations → Select app → Delete
   ```

4. **Archive in CMDB**
   - Document app deletion in configuration management DB
   - Update service catalog

### Prevention
- Implement app lifecycle policy requiring owner to re-certify annually
- Set app expiration dates (2-3 years)
- Enforce naming convention: `{team}-{purpose}-{environment}`

---

## Unused Service Principals

### Steps to Remediate

1. **Confirm Lack of Use**
   - Check audit logs for any sign-in activity (last 180+ days)
   - Review any associated applications

2. **Contact Application Owner**
   - Send notification 30 days before decommission
   - Request confirmation or plan for reactive activation

3. **Disable Service Principal** (first step)
   ```
   Azure Portal → Enterprise applications → Select SP → Properties → Enabled: No
   ```

4. **Delete Service Principal** (after 30-day grace period)
   ```
   Azure Portal → Enterprise applications → Select SP → Delete
   ```

5. **Remove Access Assignments**
   - Remove service principal from all role assignments
   - Delete associated credentials

### Timeline
- **Day 0:** Identify unused service principals
- **Day 1:** Send notification to owner
- **Day 30:** Disable service principal
- **Day 60:** Delete service principal and credentials

---

## Weak MFA Configuration

### Steps to Remediate

1. **Enable Passwordless Sign-In**
   - **Windows Hello for Business**
     ```
     Azure Portal → Devices → Device settings → Users may register their devices
     ```
   - **FIDO2 Security Keys**
     ```
     Azure Portal → Security → Authentication methods → FIDO2 security key
     Enable and set registration requirements
     ```
   - **Microsoft Authenticator App**
     ```
     Azure Portal → Security → Authentication methods → Microsoft Authenticator
     Enable and require for all users
     ```

2. **Enforce MFA Organization-Wide**
   ```
   Conditional Access → Create Policy → All users → Require multi-factor authentication
   ```

3. **Configure MFA Registration Enforcement**
   ```
   Azure Portal → Security → MFA → Require registration → Users required to register → All
   ```

4. **Monitor Enrollment**
   - Track adoption rates
   - Provide training for non-compliant users

### Rollout Timeline
- **Week 1:** Enable passwordless methods (soft launch)
- **Week 2-3:** Email campaign + training
- **Week 4:** Require MFA for high-risk operations
- **Week 8:** Enforce MFA organization-wide

---

## No Conditional Access Policies

### Steps to Remediate

### Minimum Policies to Implement

**Policy 1: Block Legacy Authentication**
```
Target: All users
Conditions: Client apps → Exchange ActiveSync clients + Other clients
Control: Block
```

**Policy 2: Require MFA for Risky Sign-Ins**
```
Target: All users
Conditions: Sign-in risk level → High, Medium
Control: Require multi-factor authentication
```

**Policy 3: Require Compliant Devices**
```
Target: All users
Conditions: Device state → Non-compliant
Control: Require device to be marked as compliant
```

**Policy 4: Block Unusual Locations**
```
Target: Sensitive users (Admin)
Conditions: Location → Any location except trusted
Control: Block
```

### Implementation Steps

1. **Review Requirements**
   - Identify sensitive apps and data
   - Define risk appetite
   - Plan user communication

2. **Create Policies in Pilot**
   ```
   Azure Portal → Security → Conditional Access → New policy
   ```

3. **Test with Report-Only Mode**
   - Set policy to "Report-only"
   - Monitor for 1 week to identify false positives

4. **Enable Policy**
   - Set to "On"
   - Monitor sign-in logs for issues

5. **Expand Progressively**
   - Week 1: Pilot with IT team
   - Week 2-3: Pilot with department
   - Week 4+: Organization-wide rollout

### Monitoring
- Azure AD Sign-in logs (Azure Portal → Azure AD → Sign-in logs)
- Conditional Access Insights dashboard
- Configure alerts for policy triggers

---

## Quick Remediation Checklist

- [ ] Schedule quarterly Entra ID security reviews
- [ ] Assign findings to department owners
- [ ] Set remediation SLAs (e.g., Critical: 7 days, High: 30 days)
- [ ] Document all changes in change management system
- [ ] Implement preventive controls (policies, templates)
- [ ] Train teams on secure practices
- [ ] Monitor compliance through automated scans
