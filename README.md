# Expense Tracker (`python-csv-expense-logger`)

A command-line Python expense tracker built for **Task 02** of the Python Programming Internship. It records daily expenses, validates inputs, summarizes spending by category, and exports the records into a spreadsheet-ready CSV file.

## Features
- **Dictionary-Based Storage:** Stores each expense entry as a structured dictionary containing `date`, `category`, and `amount`.
- **Input Validation:** Verifies that dates follow a valid format and amounts are valid positive numbers before saving.
- **Category Summaries:** Aggregates and displays total spending broken down by category.
- **CSV Export:** Writes all validated expense records to a local `.csv` file that can be opened directly in Excel, Google Sheets, or LibreOffice Calc.

## Project Structure
- `project 002.py` — Main Python script handling user input, validation, category aggregation, and CSV generation.
- `expenses.csv` — Generated output file containing the recorded expense rows.

## How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Kgmspk/python-csv-expense-logger.git](https://github.com/Kgmspk/python-csv-expense-logger.git)
   cd python-csv-expense-logger
