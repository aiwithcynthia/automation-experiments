# Payroll Validation Demo
# Created by Cynthia Perez

employees = [
    {"name": "Employee A", "hours": 40},
    {"name": "Employee B", "hours": 45},
    {"name": "Employee C", "hours": 38},
]

for employee in employees:
    if employee["hours"] > 40:
        print(f"Review overtime: {employee['name']} ({employee['hours']} hours)")
