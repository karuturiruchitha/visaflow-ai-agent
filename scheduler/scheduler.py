from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from agent.visaflow_agent import run_agent

scheduler = BlockingScheduler()

# Run every day at 8 AM
scheduler.add_job(
    run_agent,
    CronTrigger(hour=8, minute=0),
    id="daily_visa_check",
    name="Daily Visa Compliance Check"
)

# Run full report every Monday at 9 AM
scheduler.add_job(
    run_agent,
    CronTrigger(day_of_week="mon", hour=9, minute=0),
    id="weekly_report",
    name="Weekly Compliance Report"
)

if __name__ == "__main__":
    print("VisaFlow AI Agent Scheduler started...")
    print("Daily check: 8:00 AM")
    print("Weekly report: Monday 9:00 AM")
    scheduler.start()
