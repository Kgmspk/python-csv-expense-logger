import csv
from datetime import datetime
import os

CSV_FILE = "expenses.csv"
FIELDNAMES = ["date", "category", "amount"]


def validate_date(date_str):
    """Checks if the date matches YYYY-MM-DD format."""
    try:
        datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def validate_amount(amount_str):
    """Checks if the amount is a valid positive number."""
    try:
        val = float(amount_str)
        return val > 0
    except ValueError:
        return False


def load_existing_expenses():
    """Loads existing rows as dictionaries if the CSV already exists."""
    expenses = []
    if os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode="r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["amount"] = float(row["amount"])
                expenses.append(row)
    return expenses


def save_expenses(expenses):
    """Writes all expense dictionaries to the CSV file."""
    with open(CSV_FILE, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(expenses)


def add_expense(expenses):
    """Prompts user for input, validates it, and appends a dictionary."""
    while True:
        date_input = input("Enter date (YYYY-MM-DD): ").strip()
        if validate_date(date_input):
            break
        print("Invalid date. Please use YYYY-MM-DD (e.g., 2026-11-17).")

    category_input = input("Enter category (e.g., Food, Travel, Study): ").strip().title()
    if not category_input:
        category_input = "General"

    while True:
        amount_input = input("Enter amount: ").strip()
        if validate_amount(amount_input):
            amount_val = round(float(amount_input), 2)
            break
        print("Invalid amount. Enter a positive number.")

    # Store row as a dictionary
    entry = {
        "date": date_input,
        "category": category_input,
        "amount": amount_val
    }
    expenses.append(entry)
    save_expenses(expenses)
    print(f"Saved: {entry['date']} | {entry['category']} | {entry['amount']:.2f}\n")


def show_category_totals(expenses):
    """Calculates and displays total spending per category."""
    if not expenses:
        print("\nNo expenses recorded yet.\n")
        return

    totals = {}
    for item in expenses:
        cat = item["category"]
        totals[cat] = totals.get(cat, 0.0) + item["amount"]

    print("\n--- Spending by Category ---")
    for category, total in totals.items():
        print(f"{category}: {total:.2f}")
    print(f"Total Overall: {sum(totals.values()):.2f}\n")


def main():
    expenses = load_existing_expenses()
    print("=== Expense Tracker ===")

    while True:
        print("1. Add an expense")
        print("2. View totals by category")
        print("3. Save & Exit")
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            show_category_totals(expenses)
        elif choice == "3":
            save_expenses(expenses)
            print(f"All records saved to {CSV_FILE}. Exiting.")
            break
        else:
            print("Invalid choice. Enter 1, 2, or 3.\n")


if __name__ == "__main__":
    main()
