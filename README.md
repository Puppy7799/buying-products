# Advanced Python Expense Tracker

A desktop and command-line application that tracks income and expenses, stores them in JSON, calculates a balance, filters by category, and exports records to CSV. It uses only Python's standard library.

## Requirements
- Python 3.10 or newer
- No `pip install` required

## Run
1. Extract the ZIP file.
2. Open the extracted `advanced_python_expense_tracker` folder in VS Code.
3. Open Terminal → New Terminal.
4. Run the desktop interface:

   ```bash
   python main.py
   ```

   On some Windows setups, use `py main.py`.
5. To use the command-line interface instead, run:

   ```bash
   python main.py --cli
   ```

## Desktop interface

The Tkinter window provides income and expense entry, summary cards, a searchable
transaction table, category filtering, and CSV export. Enter a date as
`YYYY-MM-DD` or leave it blank to use today's date.

## Command-line menu

1. Add expense
2. Add income
3. List transactions
4. Show summary
5. Filter by category
6. Export transactions to CSV
0. Exit

Transactions are saved in `data/transactions.json`. CSV export is saved to `data/transactions.csv`.

## Advanced concepts demonstrated
- **Classes and objects:** `Expense`, `Income`, `ExpenseManager`, `JSONStorage`
- **Abstraction:** `Transaction` is an abstract base class with abstract members
- **Inheritance:** `Expense` and `Income` inherit from `Transaction`
- **Polymorphism:** `signed_amount()` and `kind` behave differently for income and expense
- **Encapsulation:** transaction amount is stored in `__amount` and exposed through a read-only property
- **Magic methods:** `__str__`, `__repr__`, `__len__`, `__iter__`, `__contains__`
- **Decorator:** `@log_action` logs when the menu is displayed
- **Generators/iterators:** `iter_transactions()` yields records lazily; manager implements `__iter__`
- **Modules/packages:** code is separated into the `tracker` package
- **Exception handling:** custom exceptions and input/storage validation
- **File handling:** JSON persistence and CSV export
- **Clean coding:** descriptive names, docstrings, small modules, and standard-library-only dependencies

## Project structure

```text
advanced_python_expense_tracker/
├── main.py
├── tracker/
│   ├── __init__.py
│   ├── exceptions.py
│   ├── gui.py
│   ├── manager.py
│   ├── models.py
│   ├── storage.py
│   └── utils.py
├── data/
│   └── transactions.json
├── requirements.txt
├── .gitignore
└── README.md
```

## Quick test
Run the app, choose `1`, and enter:
- Title: Lunch
- Amount: 150
- Category: Food
- Date: leave blank

Then choose `4` to see the summary and `0` to exit. Run the app again; the expense will still be there.
