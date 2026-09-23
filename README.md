# VisaFlow AI Compliance Agent 🛂

An autonomous AI agent that monitors employee visa expiry, 
drafts personalized compliance alerts, and generates weekly 
HR reports — built on top of the production **VisaFlow** 
immigration management system.

## What It Does

The agent runs on a schedule and autonomously:

1. 🔍 **Scans the database** — queries all employee visa records
2. ⚠️ **Identifies at-risk employees** — expiring in 30, 60, 90 days
3. 📧 **Drafts personalized emails** — individual alert per employee using Claude API
4. 📊 **Detects anomalies** — unusual expiry clusters, missing documents
5. 📋 **Generates weekly HR report** — full compliance summary for leadership
6. 🚨 **Escalates critical cases** — flags employees already expired

## Architecture

```
Scheduled trigger (daily 8 AM)
          ↓
Agent queries MySQL visa database
          ↓
Filters employees by expiry window:
  ├── 🔴 Expired — immediate action
  ├── 🟠 30 days — urgent
  ├── 🟡  60 days — warning  
  └── 🟢 90 days — monitor
          ↓
Claude API drafts personalized email per employee
          ↓
Anomaly detector flags unusual patterns
          ↓
Weekly compliance report generated
          ↓
HR leadership notified via email
```

## Sample Output

```
📊 VisaFlow AI Weekly Compliance Report
Week of: 22 Sep 2026

🔴 EXPIRED (2 employees)
  - John Smith — H1B expired 5 days ago
  - Sarah Lee — L1 expired 2 days ago

🟠 EXPIRING IN 30 DAYS (8 employees)
  - Michael Johnson — H1B expires 15 Oct 2026
  - Priya Sharma — H4 EAD expires 18 Oct 2026
  ...

⚠️ ANOMALY DETECTED
  - Unusual cluster: 12 H1B visas expiring same week (Nov 3)
  - Recommended action: Initiate batch renewal process

✅ COMPLIANT: 1,484 employees
📈 Compliance Rate: 98.7%
```

## Tech Stack

| Layer | Technology |
|---|---|
| AI Brain | Claude API (Anthropic) |
| Agent Framework | LangChain + ReAct |
| Scheduler | Python APScheduler |
| Backend | FastAPI |
| Database | MySQL |
| Email | SMTP / SendGrid |

## Setup

```bash
git clone https://github.com/karuturiruchitha/visaflow-ai-agent
cd visaflow-ai-agent
pip install -r requirements.txt
cp .env.example .env
# Add credentials to .env
python agent/visaflow_agent.py
```

## Environment Variables

```env
ANTHROPIC_API_KEY=your_claude_api_key
DB_HOST=localhost
DB_NAME=visaflow_db
DB_USER=root
DB_PASSWORD=your_password
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASSWORD=your_app_password
HR_EMAIL=hr@company.com
```

## Background

This agent extends the production **VisaFlow** immigration 
management system — a full-stack enterprise application 
(React + Spring Boot + MySQL) built for 1,500+ employees 
with Microsoft Azure AD SSO, bulk CSV import, and automated 
compliance tracking.

The AI agent adds autonomous decision-making and natural 
language generation on top of the existing infrastructure.

## Status

🚧 **In active development** — core agent and database 
integration complete. Email sending and React dashboard in progress.

## Author

**Ruchitha Karuturi** — Full Stack Developer & AI Integration Specialist  
[LinkedIn](https://linkedin.com/in/ruchitha-karuturi-51a49b24a) | 
[GitHub](https://github.com/karuturiruchitha)
