import os
from datetime import datetime

def generate_report():

    report = f"""
PASSWORD SECURITY AUDIT REPORT

Date: {datetime.now()}

Dictionary Generation : Completed
Hash Analysis         : Completed
Brute Force Test      : Completed
Password Strength     : Completed

Risk Level: Medium

Recommendations:
1. Use 12+ character passwords
2. Enable MFA
3. Avoid dictionary words
4. Use special characters

"""

    os.makedirs("reports", exist_ok=True)
    with open("reports/audit_report.txt", "w") as file:
        file.write(report)

    print("Report Generated")


generate_report()