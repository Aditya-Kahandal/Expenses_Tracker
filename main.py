# Expenses Tracker Application
"""
Inputs And Data to Handle:
automate: Data/Time (TimeStamp of the expense)
inputs: name, amount, category of the expense

functions needed: 
function to collect the name, amount, category to store in a dictionary

# For tracking the balance: for each expense, operate the balance by subtract or add according to category
"""
id = 0
def add_expense(name, amount, category, expenses, id):
    expenses[id] = {"name": name, "amount": amount, "category": category}
    id += 1
    return id
            
expenses = {}
id = add_expense("Buy Coffee", 100, "Spent", expenses,id)
id = add_expense("Buy Coffee", 100, "Spent", expenses,id)
id = add_expense("Bajaj Stocks", 4000, "Invest", expenses,id)

print(expenses)

