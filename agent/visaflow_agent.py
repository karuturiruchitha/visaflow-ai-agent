import os
import json
from anthropic import Anthropic
from dotenv import load_dotenv
from tools.visa_checker import check_expiring_visas
from tools.alert_drafter import draft_alert_email
from tools.report_generator import generate_weekly_report
from tools.anomaly_detector import detect_anomalies

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """
You are a visa compliance AI agent for an enterprise HR system.
Your job is to help HR teams manage employee visa compliance.

You have access to these tools:
- check_expiring_visas: Query database for at-risk visas
- draft_alert_email: Write personalized email for an employee
- detect_anomalies: Find unusual patterns in visa data
- generate_weekly_report: Create weekly compliance summary

Always think step by step:
1. First check who needs attention
2. Draft personalized alerts for urgent cases
3. Look for anomalies or patterns
4. Summarize everything in a report

Be professional, accurate, and compassionate in all communications.
Never share one employee's visa details with another.
"""

def run_agent():
    """Main agent loop — runs daily compliance check."""
    print("VisaFlow AI Agent starting compliance check...")

    messages = [{
        "role": "user",
        "content": """Run the daily visa compliance check:
        1. Find all employees with visas expiring in 90 days
        2. Draft personalized alert emails for those expiring in 30 days
        3. Check for any anomalies or unusual patterns
        4. Generate the weekly compliance report
        
        Start now."""
    }]

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=2000,
        system=SYSTEM_PROMPT,
        messages=messages
    )

    print("Agent response:")
    print(response.content[0].text)
    return response.content[0].text

if __name__ == "__main__":
    run_agent()
