# Expenses Tracker Application

# Function to add expenses
def add_expense(name, amount, category, expenses, transaction_id, user_balance):
    # category validation
    if category == "income" or category == "invest_sell":
        user_balance += amount
    elif category == "spend" or category == "invest_buy":
        user_balance -= amount
    else: 
        print("Wrong category")
        return transaction_id,user_balance
    expenses[transaction_id] = {"name": name, "amount": amount, "category": category}
        
    transaction_id += 1
    return transaction_id,user_balance
       
# Function to view transaction
def view_transactions(history):
    if not history:
        print("\nNo transactions made yet\n")
    else:
        print("\nYour transaction history is as follows:\n",history, "\n")

# Function to delete transaction
def delete_transactions(expenses, transaction_id, user_balance):
    if expenses[transaction_id]["category"] == "income" or expenses[transaction_id]["category"] == "invest_sell":
        user_balance -= expenses[transaction_id]["amount"]
    elif expenses[transaction_id]["category"] == "spend" or expenses[transaction_id]["category"] == "invest_buy":
        user_balance += expenses[transaction_id]["amount"]
    else: 
        print("Couldn't delete the transaction, Something went wrong")
    
    expenses.pop(transaction_id)
    return user_balance

# Updation of the transaction

def update_transaction(expenses, transaction_id , name, category, amount, user_balance):
    if expenses[transaction_id]["category"] == "income" or expenses[transaction_id]["category"] == "invest_sell":
        temp = user_balance - expenses[transaction_id]["amount"]
    else:
        temp = user_balance + expenses[transaction_id]["amount"]
    
    expenses[transaction_id]["category"] = category
    expenses[transaction_id]["amount"] = amount
    expenses[transaction_id]["name"] = name

    if category == "income" or category== "invest_sell":
        user_balance = temp + amount
    else:
        user_balance = temp - amount
    
    return user_balance
        


# HELPER Functions

def menu_display():
    print("\n\nWhat do you want to do?")
    print("1. Add Transaction")
    print("2. View Balance")
    print("3. Transaction History")
    print("4. Delete Transaction")
    print("5. Update Transaction")
    print("6. Exit")

def get_valid_id(expenses):
    while True:
        try:
            transaction_id = int(input("Enter the transaction id: "))
            if transaction_id in expenses:
                break
            else:
                print("ID not found, Try again.")
        except ValueError:
            print("You entered wrong Id, Try again")
    return transaction_id

def get_valid_amount():
    while True:
        try:
            amount = int(input("\nAmount of Transaction:"))
            break
        except ValueError:
            print("Invalid input. Please Enter the correct Value")
    return amount

def get_valid_category(transaction_type):
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

    return transaction_type[category-1]

def transaction_info(transaction_type):
    name = input("Transaction Name: ")
    amount = get_valid_amount()
    category = get_valid_category(transaction_type)

    return name, amount, category

# Implementation of user interaction flow.

flag = True
transaction_type = ["income", "spend", "invest_buy", "invest_sell" ]
transaction_id = 0
while True:
    try:
        user_balance = int(input("Enter Your Current Balance:"))
        break
    except ValueError:
        print("Invalid input, Enter Your Balance")
expenses = {}
while True:
    
    menu_display()

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid Choice, Try again")
        continue
    
    match choice:
        case 1:
            print("\n\nTo Add a transaction, Fill the following information:")
            name, amount, category = transaction_info(transaction_type)

            transaction_id,user_balance = add_expense(name, amount, category, expenses, transaction_id , user_balance)
        
        case 2: 
            print("\n\nYour current Balance is: ", user_balance)

        case 3:
            view_transactions(expenses)

        case 4:
            # Code for Deleting Transaction
            print("Enter the following details to delete your transaction:\n")
            """Either take id / name & category. We will take transaction id"""
            
            delete_id = get_valid_id(expenses)

            user_balance = delete_transactions(expenses, delete_id , user_balance)
            print("Transaction deleted successfully\n")
        case 5:
            # updation code.

            if not expenses:
                print("\nYour transaction history is empty!! You cannot update any transaction\n")

            else:
                print("\nEnter details for updating the transaction:\n")
                update_id = get_valid_id(expenses)
                name, amount, category = transaction_info(transaction_type)
                user_balance = update_transaction(expenses, update_id , name, category, amount, user_balance)
            
        case 6:
            break
        case _ :
            print("No such action to perform.")