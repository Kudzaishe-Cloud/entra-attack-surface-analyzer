# -*- coding: utf-8 -*-
import json
import csv
import sys
from datetime import datetime, timezone
from typing import List, Dict, Any
from pathlib import Path

sys.stdout.reconfigure(encoding='utf-8')

class Reporter:
    """Generate reports in JSON and CSV format"""

    @staticmethod
    def generate_json_report(findings: List[Dict], output_dir: str = "./reports") -> str:
        """Generate JSON report"""
        Path(output_dir).mkdir(exist_ok=True)

        report = {
            "scan_date": datetime.now(timezone.utc).isoformat(),
            "total_findings": len(findings),
            "findings_by_severity": {
                "CRITICAL": len([f for f in findings if f["severity"] == "CRITICAL"]),
                "HIGH": len([f for f in findings if f["severity"] == "HIGH"]),
                "MEDIUM": len([f for f in findings if f["severity"] == "MEDIUM"]),
                "LOW": len([f for f in findings if f["severity"] == "LOW"])
            },
            "findings": findings
        }

        filepath = f"{output_dir}/entra-attack-surface-{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filepath, 'w') as f:
            json.dump(report, f, indent=2)

        print(f"✅ JSON report saved: {filepath}")
        return filepath

    @staticmethod
    def generate_csv_report(findings: List[Dict], output_dir: str = "./reports") -> str:
        """Generate CSV report"""
        Path(output_dir).mkdir(exist_ok=True)

        filepath = f"{output_dir}/entra-attack-surface-{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"

        with open(filepath, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=["severity", "type", "resource", "description", "remediation"])
            writer.writeheader()
            for finding in findings:
                writer.writerow(finding)

        print(f"✅ CSV report saved: {filepath}")
        return filepath

    @staticmethod
    def print_summary(findings: List[Dict]):
        """Print summary to console"""
        critical = len([f for f in findings if f["severity"] == "CRITICAL"])
        high = len([f for f in findings if f["severity"] == "HIGH"])
        medium = len([f for f in findings if f["severity"] == "MEDIUM"])

        print("\n" + "="*60)
        print(f"ENTRA ID ATTACK SURFACE ANALYSIS REPORT")
        print(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("="*60)
        print(f"Total Findings: {len(findings)}")
        print(f"🔴 Critical: {critical}")
        print(f"🟠 High: {high}")
        print(f"🟡 Medium: {medium}")
        print("="*60 + "\n")

        for finding in findings:
            severity_icon = {"CRITICAL": "🔴", "HIGH": "🟠", "MEDIUM": "🟡", "LOW": "🟢"}.get(finding["severity"], "⚪")
            print(f"{severity_icon} [{finding['type']}] {finding['resource']}")
            print(f"   → {finding['description']}")
            print(f"   ✓ {finding['remediation']}\n")
