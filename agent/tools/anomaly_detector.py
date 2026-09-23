import os
from anthropic import Anthropic
from collections import Counter
from dotenv import load_dotenv
import json

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def detect_anomalies(visa_data: dict) -> str:
    """
    Detect unusual patterns in visa expiry data
    using statistical analysis + Claude AI interpretation.
    """
    all_employees = (
        visa_data.get("expired", []) +
        visa_data.get("critical_30", []) +
        visa_data.get("warning_60", []) +
        visa_data.get("monitor_90", [])
    )

    # Statistical analysis
    visa_types = Counter(e["visa_type"] for e in all_employees)

    expiry_months = Counter()
    for emp in all_employees:
        if emp.get("expiry_date"):
            month = str(emp["expiry_date"])[:7]
            expiry_months[month] += 1

    stats = {
        "total_at_risk": len(all_employees),
        "by_visa_type": dict(visa_types),
        "by_expiry_month": dict(expiry_months),
        "expired_count": len(visa_data.get("expired", [])),
        "critical_count": len(visa_data.get("critical_30", []))
    }

    # Claude interprets the patterns
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=400,
        system="""You are a visa compliance analyst.
Identify unusual patterns that HR should know about.
Look for: unusual clusters, high concentration of one visa type,
multiple expirations same week, sudden spikes.
Be concise and actionable.""",
        messages=[{
            "role": "user",
            "content": f"Analyze these visa expiry statistics for anomalies:\n{json.dumps(stats, indent=2)}"
        }]
    )

    return response.content[0].text
