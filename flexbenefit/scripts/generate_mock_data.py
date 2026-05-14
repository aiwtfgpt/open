import csv
import json
import random
from datetime import datetime, timedelta

def generate_mock_data(num_employees=50):
    employees = []
    base_date = datetime(2024, 1, 1)
    
    for i in range(1, num_employees + 1):
        emp_id = f"EMP{i:04d}"
        first_name = random.choice(["James", "Mary", "Robert", "Patricia", "John", "Jennifer", "Michael", "Linda"])
        last_name = random.choice(["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis"])
        
        # Payroll info
        salary = random.randint(45000, 120000)
        current_payroll_deduction = round(random.uniform(0, 41.67), 2)
        
        # Mock enrollment status (some have already selected benefits)
        # Total cap is 41.67. 
        # We simulate partial selections to test the math logic.
        existing_deduction = round(random.uniform(0, 30.00), 2) if random.random() > 0.5 else 0.0
        
        employees.append({
            "employee_id": emp_id,
            "first_name": first_name,
            "last_name": last_name,
            "email": f"{first_name.lower()}.{last_name.lower()}{i}@example.com",
            "annual_salary": salary,
            "current_payroll_deduction": existing_deduction,
            "available_flex_spend": round(41.67 - existing_deduction, 2),
            "last_updated": (base_date + timedelta(days=random.randint(0, 365))).strftime("%Y-%m-%d"),
            "status": "active"
        })
    
    return employees

if __name__ == "__main__":
    data = generate_mock_data(50)
    
    # Save to CSV for easy ledger simulation
    with open('~/flexbenefit/data/mock_employees/employees.csv', 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
        
    # Save to JSON for n8n/API simulation
    with open('~/flexbenefit/data/mock_employees/employees.json', 'w') as f:
        json.dump(data, f, indent=4)

    print(f"Successfully generated mock data for {len(data)} employees.")
