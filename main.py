"""Command-line entry point for the Advanced Python Expense Tracker."""
import argparse
from datetime import date
from tracker.manager import ExpenseManager
from tracker.models import Expense, Income
from tracker.storage import JSONStorage
from tracker.utils import configure_console_encoding, log_action
from tracker.exceptions import TrackerError


configure_console_encoding()


@log_action
def show_menu():
    print("\n=== ADVANCED PYTHON EXPENSE TRACKER ===")
    print("1. Add expense")
    print("2. Add income")
    print("3. List transactions")
    print("4. Show summary")
    print("5. Filter by category")
    print("6. Export transactions to CSV")
    print("0. Exit")
    try:
        return input("Choose an option: ").strip()
    except EOFError:
        print("\nInput stream closed. Exiting gracefully.")
        raise SystemExit(0)


def run_cli():
    manager = ExpenseManager(JSONStorage("data/transactions.json"))
    manager.load()
    print("Welcome! Your transactions are saved automatically.")
    try:
        while True:
            choice = show_menu()
            try:
                if choice == "1":
                    title = input("Expense title: ").strip()
                    amount = float(input("Amount (₹): "))
                    category = input("Category (e.g. Food, Travel): ").strip()
                    tx_date = input("Date YYYY-MM-DD (blank=today): ").strip()
                    tx_date = date.fromisoformat(tx_date) if tx_date else date.today()
                    manager.add(Expense(title, amount, category, tx_date))
                    print("Expense saved.")
                elif choice == "2":
                    title = input("Income source: ").strip()
                    amount = float(input("Amount (₹): "))
                    category = input("Category (e.g. Salary, Freelance): ").strip()
                    tx_date = input("Date YYYY-MM-DD (blank=today): ").strip()
                    tx_date = date.fromisoformat(tx_date) if tx_date else date.today()
                    manager.add(Income(title, amount, category, tx_date))
                    print("Income saved.")
                elif choice == "3":
                    transactions = list(manager.iter_transactions())
                    if not transactions:
                        print("No transactions found.")
                    for item in transactions:
                        print(item)
                elif choice == "4":
                    summary = manager.summary()
                    print(f"Total income:   ₹{summary['income']:.2f}")
                    print(f"Total expenses: ₹{summary['expenses']:.2f}")
                    print(f"Balance:        ₹{summary['balance']:.2f}")
                    print(f"Transactions:   {summary['count']}")
                elif choice == "5":
                    category = input("Category to find: ").strip()
                    found = list(manager.by_category(category))
                    for item in found:
                        print(item)
                    if not found:
                        print("No matching transactions.")
                elif choice == "6":
                    path = manager.export_csv("data/transactions.csv")
                    print(f"Exported to {path}")
                elif choice == "0":
                    print("Goodbye!")
                    break
                else:
                    print("Please choose one of the listed options.")
            except (EOFError, KeyboardInterrupt):
                print("\nInput interrupted. Exiting the app.")
                break
            except (ValueError, TrackerError, OSError) as exc:
                print(f"Could not complete that action: {exc}")
    except (EOFError, KeyboardInterrupt):
        print("\nSession closed.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Advanced Python Expense Tracker")
    parser.add_argument(
        "--cli", action="store_true", help="run the command-line interface"
    )
    arguments = parser.parse_args()
    if arguments.cli:
        run_cli()
    else:
        from tracker.gui import run_gui

        run_gui()
