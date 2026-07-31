# Expenses Tracker Application
"""
Inputs And Data to Handle:
automate: Data/Time (TimeStamp of the expense)
inputs: name, amount, category of the expense

functions needed: 
function to collect the name, amount, category to store in a dictionary

# For tracking the balance: for each expense, operate the balance by subtract or add according to category
"""

def add_expense(name, amount, category, expenses, id, User_Balance):
    # category validation
    if category == "income":
        User_Balance += amount
    elif category == "spend":
        User_Balance -= amount
    elif category == "invest_buy":
        User_Balance -= amount
    elif category == "invest_sell":
        User_Balance += amount
    else: 
        print("Wrong category")
        return id,User_Balance
    expenses[id] = {"name": name, "amount": amount, "category": category}
        
    id += 1
    return id,User_Balance
       
def viewTransactions(history):
    if history == {}:
        print("\nNo transactions made yet\n")
    else:
        print("\nYour transaction history is as follows:\n",history, "\n")


# Implementation of user interaction flow.

flag = True
transactionType = ["income", "spend", "invest_buy", "invest_sell" ]
id = 0
while True:
    try:
        User_Balance = int(input("Enter Your Current Balance:"))
        break
    except ValueError:
        print("Invalid input, Enter Your Balance")
expenses = {}
while flag:
    print("\n\nWhat do you want to do?")
    print("1. Add Transaction")
    print("2. View Balance")
    print("3. Transaction History")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid Choice, Try again")
        continue
    
    match choice:
        case 1:
            print("\n\nTo Add a transaction, Fill the following information:")
            name = input("\nTransaction info: ")
            while True:
                try:
                    amount = int(input("\nAmount of Transaction:"))
                    break
                except ValueError:
                    print("Invalid input. Please Enter the correct Value")

            while True:
                try:
                    category = int(input("\nType of Transaction:\n1. Income / Salary / Savings \n2. Spendings / Expenses \n3. Buying Stocks / Shares. \n4. Selling Stocks / Shares. \nEnter Your Choice: "))
                    if category > 0 and category<5: 
                        break
                    else:
                        print("Invalid choice. Please enter a valid choice.")
                        continue
                except ValueError:
                    print("Invalid choice. Please enter a valid choice.")
            id,User_Balance = add_expense(name, amount, transactionType[category-1], expenses, id , User_Balance)
        
        case 2: 
            print("\n\nYour current Balance is: ", User_Balance)

        case 3:
            viewTransactions(expenses)

        case 4:
            flag = False
        case _ :
            print("No such action to perform.")
