# FlexBenefit Project

This project contains automation workflows and scripts for managing employee benefits and account usage.

## Directory Structure

- **data/**: Contains mock employee data (JSON and CSV formats) used for testing and simulation.
- **scripts/**: Python scripts for data processing and logic testing.
  - `generate_mock_data.py`: Generates mock employee datasets.
  - `find_underused_accounts.py`: Identifies accounts with low engagement.
  - `test_logic_sim.py`: Simulates benefit logic.
- **workflows/**: n8n workflow definitions for automating business processes.
  - `ecosystem_sync.json`: Syncs data across the benefit ecosystem.
  - `enrollment_logic.json`: Manages the benefits enrollment process.
  - `outbound_nudges.json`: Triggers automated nudges for underused benefits.
  - `user_form.json`: Handles user input forms.

## Setup & Usage

The workflows in this directory are designed to be imported into **n8n**. 

### Running Scripts
Most scripts require the mock data found in `data/mock_employees/`.

```bash
# Example: Generate new mock data
python3 scripts/generate_mock_data.py
```

### n8n Integration
The workflows are triggered or executed via the command line or n8n's internal scheduling, often interacting with the local Python scripts.
