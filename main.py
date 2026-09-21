# -*- coding: utf-8 -*-
import os
import sys
from dotenv import load_dotenv
from modules.graph_client import GraphAPIClient
from modules.checks import VulnerabilityChecks
from modules.reporters import Reporter

sys.stdout.reconfigure(encoding='utf-8')
load_dotenv()

def main():
    print("🚀 Starting Entra ID Attack Surface Analysis...\n")

    # Step 1: Authenticate
    client = GraphAPIClient()
    client.authenticate()

    # Step 2: Collect data
    print("📊 Collecting data from Entra ID...")
    users = client.get_all_users()
    apps = client.get_all_applications()
    sps = client.get_service_principals()
    ca_policies = client.get_conditional_access_policies()
    auth_policy = client.get_authentication_methods_policy()

    print(f"   Found {len(users)} users")
    print(f"   Found {len(apps)} applications")
    print(f"   Found {len(sps)} service principals")
    print(f"   Found {len(ca_policies)} CA policies\n")

    # Step 3: Run checks
    print("🔍 Running security checks...")
    checks = VulnerabilityChecks()
    findings = checks.run_all_checks(users, apps, sps, ca_policies, auth_policy)

    # Step 4: Generate reports
    print("📝 Generating reports...")
    output_dir = os.getenv("OUTPUT_DIR", "./reports")

    Reporter.generate_json_report(findings, output_dir)
    Reporter.generate_csv_report(findings, output_dir)
    Reporter.print_summary(findings)

    print(f"✅ Analysis complete! Reports saved to {output_dir}/")

if __name__ == "__main__":
    main()
