def sample():
    print("Welcome")
def addition(a,b):
    print(f"Addition of a ={a} b={b} and c={a+b}")
def login(username):
    print(f"Dear {username},Welcome to goodvibes") 
def logout():
    print("You are logout successfully")
balance_amount=50000 #global variable
def credit(amount):
    global balance_amount
    balance_amount+=amount
    print("Current balance amount is",balance_amount)
    