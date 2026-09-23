# VisaFlow AI Agent — Architecture

## System Overview

```
Scheduler (APScheduler)
        ↓
Daily trigger at 8 AM
        ↓
visa_checker.py → MySQL query
        ↓
Categorize by urgency:
  ├── Expired (immediate)
  ├── 30 days (critical)
  ├── 60 days (warning)
  └── 90 days (monitor)
        ↓
alert_drafter.py → Claude API
→ Personalized email per employee
        ↓
anomaly_detector.py → Claude API
→ Pattern analysis on full dataset
        ↓
report_generator.py → Claude API
→ Weekly HR leadership report
        ↓
Email sent via SMTP
```

## Database Schema

```sql
CREATE TABLE employees (
  employee_id VARCHAR(20) PRIMARY KEY,
  first_name VARCHAR(100),
  last_name VARCHAR(100),
  email VARCHAR(200),
  department VARCHAR(100),
  status ENUM('ACTIVE','INACTIVE')
);

CREATE TABLE visas (
  id INT AUTO_INCREMENT PRIMARY KEY,
  employee_id VARCHAR(20),
  visa_type VARCHAR(50),
  expiry_date DATE,
  issue_date DATE,
  status ENUM('ACTIVE','EXPIRED','CANCELLED'),
  FOREIGN KEY (employee_id) REFERENCES employees(employee_id)
);
```

## Extension of Production System

This agent extends the production VisaFlow system:

| Production System | AI Agent Extension |
|---|---|
| Manual HR checks | Autonomous daily scanning |
| Generic reminder emails | Personalized Claude-drafted alerts |
| No pattern detection | Anomaly detection across 1,500+ records |
| No weekly summary | Auto-generated leadership reports |
