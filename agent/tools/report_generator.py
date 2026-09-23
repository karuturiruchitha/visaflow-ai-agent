import os
from anthropic import Anthropic
from datetime import datetime
from dotenv import load_dotenv
import json

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def generate_weekly_report(visa_data: dict, anomalies: str) -> str:
    """
    Generate a weekly visa compliance report
    for HR leadership using Claude API.
    """
    summary = {
        "week": datetime.now().strftime("%B %d, %Y"),
        "expired": len(visa_data.get("expired", [])),
        "critical_30_days": len(visa_data.get("critical_30", [])),
        "warning_60_days": len(visa_data.get("warning_60", [])),
        "monitor_90_days": len(visa_data.get("monitor_90", [])),
        "anomalies": anomalies
    }

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=800,
        system="""You are an HR compliance report writer.
Generate clear, professional weekly visa compliance reports.
Format for senior leadership — executives who need 
the key numbers and actions at a glance.
Include: summary, urgent actions, anomalies, overall compliance rate.""",
        messages=[{
            "role": "user",
            "content": f"Generate weekly compliance report from:\n{json.dumps(summary, indent=2)}"
        }]
    )

    return response.content[0].text
