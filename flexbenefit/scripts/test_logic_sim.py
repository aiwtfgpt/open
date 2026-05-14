import json
import os

def simulate_enrollment(emp_id, cost):
    base_path = "/home/handy/flexbenefit/data/mock_employees/employees.json"
    
    with open(base_path, 'r') as f:
        employees = json.load(f)
    
    user = next((e for e in employees if e['employee_id'] == emp_id), None)
    
    if not user:
        print(f"Error: Employee {emp_id} not found.")
        return

    print(f"Attempting enrollment for {user['first_name']} {user['last_name']}...")
    print(f"Selected Benefit Cost: ${cost}")
    print(f"Available Flex Spend: ${user['available_flex_spend']}")

    if cost > user['available_flex_spend']:
        print("RESULT: [REJECTED] - Insufficient Funds.")
    else:
        print("RESULT: [SUCCESS] - Enrollment Validated.")

if __name__ == "__main__":
    # Test Case 1: Valid low cost
    print("--- TEST 1: LOW COST ---")
    simulate_enrollment("EMP0001", 10.00)
    
    print("\n--- TEST 2: OVER BUDGET ---")
    # Find an employee with low balance
    with open("/home/handy/flexbenefit/data/mock_employees/employees.json", 'r') as f:
        data = json.load(f)
    poor_emp = min(data, key=lambda x: x['available_flex_spend'])
    simulate_enrollment(poor_emp['employee_id'], 40.00)
