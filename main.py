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
User_Balance = 0
def add_expense(name, amount, category, expenses, id, User_Balance):
    if category.lower() == "income":
        User_Balance += amount
    elif category.lower() == "spend":
        User_Balance -= amount
    elif category.lower() == "invest_buy":
        User_Balance -= amount
    elif category.lower() == "invest_sell":
        User_Balance += amount
    else: 
        print("Wrong category")
        return id,User_Balance
    expenses[id] = {"name": name, "amount": amount, "category": category}
        
    id += 1
    return id,User_Balance
            
expenses = {}
id,User_Balance = add_expense("Buy Coffee", 100, "Spent", expenses,id,User_Balance) 
id,User_Balance = add_expense("Buy Coffee", 100, "Spend", expenses,id,User_Balance)
id,User_Balance = add_expense("Bajaj Stocks", 4000, "Iknvest_buy", expenses,id,User_Balance)
id,User_Balance = add_expense("Bajaj Stocks", 5000, "Invest_sell", expenses,id,User_Balance)

print(expenses, User_Balance)

