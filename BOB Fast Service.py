print("\n")
a={ }
print("\n")
def display():
    print("                   BANK OF BARODA                 ")
    print("\n")
    print(" Hey Sir! , How can I help you - ")
    print("\n")
    print(" NOTE - Firstly you can create an account with minimum balance to access all features.")
    print("\n")
    print(" 1. Open a New Account")
    print(" 2. Bank Balance")
    print(" 3. Money Deposit")
    print(" 4. Money Withdrawal")
    print(" 5. Exit the Portal")
    print("\n")

def newaccount(name,balance):
    print("\n") 
    if name in a:
        print("\n")
        print(" This name is already access in our Bank please change your name to Continue!")
        print("\n")
    else:
        a[name]=balance
        print(f" Account with name- {name} is created. ")
        print("\n")

def bankbalance(name):
    if name in a:
        print("\n")
        print(" Balance available in acccount is -",a[name],"rs.")
        print("\n")
    else:
        print("\n")
        print(f" Account with name- {name} is not exist!")
        print("\n")

def moneydeposit(name,amount):
    if name in a:
        print("\n")
        a[name]=a[name]+amount
        print(" Money is Successfully deposited in your Account!")
        print("\n")
    else:
        print("\n")
        print(f" Account with name- {name} is not exist!")
        print("\n") 

def moneywithdrawal(name,amount):
    if name in a:
        print("\n")
        a[name]=a[name]-amount
        print(" Please take your Money Carefully!")
        print("\n")
    else:
        print("\n")
        print(f" Account with name- {name} is not exist!")
        print("\n") 

display()
print("\n")
while True:
    print("\n")
    b=input(" Enter which you wants(1-5) -")
    print("\n")
    if b=='1':
        name=input(" Enter the account Holder name -")
        mobile=int(input(" Enter mobile no. -"))
        balance=int(input(" Enter the opening account cash -"))
        print("\n")
        newaccount(name,balance)
    elif b=='2':
        name=input(" Enter the account Holder name -")
        print("\n")
        bankbalance(name)
    elif b=='3':
        name=input(" Enter the account Holder name -")
        amount=int(input(" Please enter the amount wants to be deposit -"))
        print("\n")
        moneydeposit(name,amount)
    elif b=='4':
        name=input(" Enter the account Holder name -")
        amount=int(input(" Please enter the amount wants to be withhdrawal -"))
        print("\n")
        moneywithdrawal(name,amount) 
    elif b=='5':
        print(" Thankyou Sir !")
        print("\n")
        break 
    else:
        print("\n")
        print(" Please enter a valid option!")
        








        



