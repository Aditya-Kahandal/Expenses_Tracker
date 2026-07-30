# Expenses Tracker Application
"""
Inputs And Data to Handle:
automate: Data/Time (TimeStamp of the expense)
inputs: name, amount, category of the expense

functions needed: 
function to collect the name, amount, category to store in a dictionary

# For tracking the balance: for each expense, operate the balance by subtract or add according to category
"""

def add_expense(name, amount, category, expenses, id):
    if id not in expenses:
        expenses[id] = {"name": name, "amount": amount, "category": category}
    else:
        if category == expenses[id]["category"] and name == expenses[id]["name"] and amount != expenses[id]["amount"]:
            expenses[id]["amount"] += amount
        else:
            print("Expense with this name and category already exists with same amount. Do you want to still add it? (yes/no)")
            user_input = input()

            if user_input.lower().strip() == "yes":
                expenses[id]["amount"] += amount
            else:
                print("Expense not added")
    return expenses
        
expenses = {}
add_expense("Buy Coffee", 100, "Spent", expenses, 1)
add_expense("Buy Coffee", 100, "Spent", expenses, 1)
add_expense("Bajaj Stocks", 4000, "Invest", expenses, 2)

print(expenses)

