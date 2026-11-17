# Python CSV Expense Logger

A lightweight Python command-line tool to log daily expenses, validate inputs, view spending totals by category, and export records to a spreadsheet-compatible CSV file.

## Features
- **Input Validation:** Verifies dates (`YYYY-MM-DD`) using Python's `datetime` module and ensures amounts are positive numbers before saving.
- **Dictionary-Based Storage:** Stores each expense row as a Python dictionary and uses `csv.DictWriter` / `csv.DictReader` for clean serialization.
- **Category Breakdown:** Aggregates and displays total spending per category directly in the terminal.

## How to Run
1. Ensure Python 3 is installed on your machine.
2. Clone this repository and navigate into the folder:
   ```bash
   git clone [https://github.com/](https://github.com/)<your-github-username>/python-csv-expense-logger.git
   cd python-csv-expense-logger
