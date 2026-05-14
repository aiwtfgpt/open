import json
import os

def find_low_balance_users(threshold=5.0):
    base_path = os.path.expanduser("~/flexbenefit/data/mock_employees/employees.json")
    
    if not os.path.exists(base_path):
        print("Error: Mock data file not found.")
        return []

    with open(base_path, 'r') as f:
        employees = json.load(f)
    
    # Find users who have less than the threshold remaining
    # or haven't used their budget at all (as an example for nudge)
    low_balance_users = [
        {
            "first_name": e["first_name"],
            "last_name": e["last_name"],
            "phone_number": f"+1555000{e['employee_id'][-3:]}", # Mock phone
            "available_flex_spend": e["available_flex_spend"]
        }
        for e in employees if e["available_flex_spend"] < threshold
    ]
    
    return low_balance_users

if __name__ == "__main__":
    # For testing purposes in Phase 3, we print the count
    # In production, this outputs JSON for n8n
    users = find_low_balance_users(threshold=10.0)
    print(json.dumps(users))
