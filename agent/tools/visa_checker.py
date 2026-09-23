import mysql.connector
import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()

def get_db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

def check_expiring_visas(days_threshold: int = 90) -> list:
    """
    Query MySQL database for employees with visas 
    expiring within the given number of days.
    Returns list of at-risk employees.
    """
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    expiry_date = datetime.now() + timedelta(days=days_threshold)
    today = datetime.now()

    query = """
        SELECT 
            e.employee_id,
            e.first_name,
            e.last_name,
            e.email,
            v.visa_type,
            v.expiry_date,
            DATEDIFF(v.expiry_date, CURDATE()) as days_remaining
        FROM employees e
        JOIN visas v ON e.employee_id = v.employee_id
        WHERE v.expiry_date <= %s
        AND v.status = 'ACTIVE'
        ORDER BY v.expiry_date ASC
    """

    cursor.execute(query, (expiry_date,))
    employees = cursor.fetchall()

    cursor.close()
    conn.close()

    # Categorize by urgency
    result = {
        "expired": [],
        "critical_30": [],
        "warning_60": [],
        "monitor_90": []
    }

    for emp in employees:
        days = emp["days_remaining"]
        if days < 0:
            result["expired"].append(emp)
        elif days <= 30:
            result["critical_30"].append(emp)
        elif days <= 60:
            result["warning_60"].append(emp)
        else:
            result["monitor_90"].append(emp)

    return result
