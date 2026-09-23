import os
from anthropic import Anthropic
from dotenv import load_dotenv

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def draft_alert_email(employee: dict) -> str:
    """
    Use Claude API to draft a personalized visa 
    expiry alert email for an employee.
    """
    days_remaining = employee.get("days_remaining", 0)
    urgency = "URGENT" if days_remaining <= 30 else "REMINDER"

    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=500,
        system="""You are an HR communications specialist.
Write professional, empathetic visa expiry alert emails.
Be clear about the deadline and next steps.
Do not include any other employee's information.
Keep emails under 150 words.""",
        messages=[{
            "role": "user",
            "content": f"""Draft a visa expiry alert email for:
            
Employee: {employee['first_name']} {employee['last_name']}
Visa Type: {employee['visa_type']}
Expiry Date: {employee['expiry_date']}
Days Remaining: {days_remaining}
Urgency Level: {urgency}

Write the complete email including subject line."""
        }]
    )

    return response.content[0].text
