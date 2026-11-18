# Expense Tracker (`python-csv-expense-logger`)

A command-line Python expense tracker built for **Task 02** of the Python Programming Internship. It records daily expenses, validates inputs, summarizes spending by category, and exports the records into a spreadsheet-ready CSV file[cite: 1, 2].

## Features
- **Dictionary-Based Storage:** Stores each expense entry as a structured dictionary containing `date`, `category`, and `amount`[cite: 1, 2].
- **Input Validation:** Verifies that dates follow a valid format and amounts are valid positive numbers before saving[cite: 1, 2].
- **Category Summaries:** Aggregates and displays total spending broken down by category[cite: 1, 2].
- **CSV Export:** Writes all validated expense records to a local `.csv` file that can be opened directly in Excel, Google Sheets, or LibreOffice Calc[cite: 1, 2].

## Project Structure
- `project 002.py` — Main Python script handling user input, validation, category aggregation, and CSV generation[cite: 2].
- `expenses.csv` — Generated output file containing the recorded expense rows[cite: 2].

## How to Run

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Kgmspk/python-csv-expense-logger.git](https://github.com/Kgmspk/python-csv-expense-logger.git)
   cd python-csv-expense-logger
