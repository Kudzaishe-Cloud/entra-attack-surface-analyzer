from typing import Dict, List, Any
from datetime import datetime, timedelta, timezone

class VulnerabilityChecks:
    """Performs security checks on Entra ID resources"""

    def __init__(self):
        self.findings = []

    def check_inactive_users(self, users: List[Dict], days_threshold: int = 90) -> List[Dict]:
        """Find users who haven't signed in recently"""
        findings = []
        cutoff_date = datetime.now(timezone.utc) - timedelta(days=days_threshold)

        for user in users:
            if not user.get("accountEnabled"):
                continue

            created = datetime.fromisoformat(user["createdDateTime"].replace("Z", "+00:00"))
            if created < cutoff_date:
                findings.append({
                    "type": "INACTIVE_USER",
                    "severity": "MEDIUM",
                    "resource": user["userPrincipalName"],
                    "description": f"User created {(datetime.now(timezone.utc) - created).days} days ago, likely inactive",
                    "remediation": "Review and disable inactive accounts per your recertification policy"
                })

        return findings

    def check_orphaned_applications(self, apps: List[Dict], sps: List[Dict]) -> List[Dict]:
        """Find registered applications with no service principals"""
        findings = []
        sp_app_ids = {sp["appId"] for sp in sps}

        for app in apps:
            if app["appId"] not in sp_app_ids:
                findings.append({
                    "type": "ORPHANED_APPLICATION",
                    "severity": "HIGH",
                    "resource": app["displayName"],
                    "description": "Registered app has no service principal—likely unused or abandoned",
                    "remediation": "Verify app is needed; delete if orphaned to reduce attack surface"
                })

        return findings

    def check_unused_service_principals(self, sps: List[Dict], days_threshold: int = 180) -> List[Dict]:
        """Find service principals that haven't been used recently"""
        findings = []
        cutoff_date = datetime.now(timezone.utc) - timedelta(days=days_threshold)

        for sp in sps:
            created = datetime.fromisoformat(sp["createdDateTime"].replace("Z", "+00:00"))

            if created < cutoff_date and not sp.get("accountEnabled"):
                findings.append({
                    "type": "UNUSED_SERVICE_PRINCIPAL",
                    "severity": "MEDIUM",
                    "resource": sp["displayName"],
                    "description": f"Service principal unused for {days_threshold}+ days and disabled",
                    "remediation": "Verify purpose; delete if no longer needed per JML process"
                })

        return findings

    def check_weak_mfa(self, auth_policy: Dict) -> List[Dict]:
        """Check if MFA is properly configured"""
        findings = []

        if not auth_policy.get("authenticationMethodConfigurations"):
            findings.append({
                "type": "WEAK_MFA_CONFIG",
                "severity": "HIGH",
                "resource": "Authentication Policy",
                "description": "No passwordless authentication methods configured; relying on passwords",
                "remediation": "Enable Windows Hello, FIDO2, or app-based authentication"
            })

        return findings

    def check_no_conditional_access(self, policies: List[Dict]) -> List[Dict]:
        """Check if Conditional Access is properly configured"""
        findings = []

        if not policies:
            findings.append({
                "type": "NO_CONDITIONAL_ACCESS",
                "severity": "CRITICAL",
                "resource": "Conditional Access",
                "description": "No Conditional Access policies configured; no risk-based access control",
                "remediation": "Implement CA policies for risky sign-ins, device compliance, and locations"
            })

        return findings

    def run_all_checks(self, users: List[Dict], apps: List[Dict], sps: List[Dict],
                       ca_policies: List[Dict], auth_policy: Dict) -> List[Dict]:
        """Run all checks and return findings"""
        all_findings = []

        all_findings.extend(self.check_inactive_users(users))
        all_findings.extend(self.check_orphaned_applications(apps, sps))
        all_findings.extend(self.check_unused_service_principals(sps))
        all_findings.extend(self.check_weak_mfa(auth_policy))
        all_findings.extend(self.check_no_conditional_access(ca_policies))

        return all_findings
