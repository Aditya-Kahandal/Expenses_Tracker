# 💰 Expense Tracker (CLI)

A command-line Expense Tracker built in Python to manage personal finances.

This project was developed from scratch as a software engineering exercise to practice application design, CRUD operations, state management, input validation, refactoring, and persistent storage using JSON.

---

## Features

- ✅ Add transactions
- ✅ View transaction history
- ✅ Update existing transactions
- ✅ Delete transactions
- ✅ Categorize transactions
  - Income
  - Spend
  - Invest Buy
  - Invest Sell
- ✅ Automatic balance calculation
- ✅ Persistent data storage using JSON
- ✅ Input validation
- ✅ Unique transaction IDs

---

## Project Structure

```
Expense_Tracker/
│
├── main.py
├── expenses_tracker.json        # Created automatically after first run
└── README.md
```

---

## Technologies Used

- Python 3.12+
- JSON
- File Handling
- Exception Handling

---

## How It Works

The application maintains three pieces of state:

- Transaction History
- Current Balance
- Next Transaction ID

When the application starts:

- Loads saved data from `expenses.json`
- If no save file exists, asks for the initial balance

When the application exits:

- Saves the complete application state to `expenses.json`

---

## Running the Project

Clone the repository

```bash
git clone <repository-url>
```

Navigate into the project

```bash
cd Expense_Tracker
```

Run

```bash
python3 main.py
```

---

## Sample Menu

```
1. Add Transaction
2. View Balance
3. Transaction History
4. Delete Transaction
5. Update Transaction
6. Exit
```

---

## Example Transaction

```
Transaction Name: Salary
Amount: 50000
Category: Income
```

---

## Engineering Concepts Practiced

This project focuses on software engineering fundamentals rather than just Python syntax.

Implemented concepts include:

- Functions
- Dictionaries
- State Management
- CRUD Operations
- Input Validation
- Helper Functions
- Refactoring
- JSON Serialization
- File Handling
- Exception Handling

---

## Future Improvements

Planned features include:

- Search transactions
- Filter by category
- Monthly summaries
- Better CLI formatting
- Modular project structure
- SQLite database
- REST API backend
- React frontend
- Authentication
- Analytics dashboard
- AI-powered financial insights

---

## Learning Goal

The objective of this project is to progressively evolve a simple CLI application into a production-style finance management system while learning software engineering concepts naturally through project development.

---

## Author

**Aditya Kahandal**

GitHub: https://github.com/Aditya-Kahandal
