#OOP PART
class NotenoughAcct(Exception): #raise an Exception when you dont have enough Accounts
    pass
class Expenditure_manager():
    id = 0
    
    def __init__(self, name:str, iAmount:int, deficiet=0):
        self.amount = name
        self.balance = iAmount
        Expenditure_manager.id +=1
        self.id = Expenditure_manager.id
    # def getCounter(self): #counts the number of users 
    #     return self.counter
    def getName(self):
        return self.name
    
    #now I have to create a send money feature
    #for that I need a deposite, withdrawal and transaction feature
    #and I need to create a function which confirms wheather and transaction is viable or not
    #also a feature which can confirm wheather there are enough accounts to do a transc
    
ACCOUNTS = {} #Approach to create dynamic new accounts and storing it in chadgpt

###############################
###############################
###############################



print("Welcome to the Expenditure manager!")
# Dave = expenditure_manager('Dave', 500)
# print(Dave.balance) #gives me the balance of Dave
# # print(Dave.id)
def createAccount():
    flag = 1
    while flag!=0:
        print("Great! What's the name of the Account? : ", end="")
        name = str(input(""))
        print("What's the initial Balance in the Account? : ", end="")
        balance = int(input(""))
        newaccount = Expenditure_manager(name, balance)
        ACCOUNTS[name] = newaccount
        print(f"New Account '{name}' created' with ID {newaccount.id} and balance: {newaccount.balance:.2f}")

def proceed():
    print("What do you wish to do?")
    print("1- Create another account? :", end="")
    print("2- Do an expenditure? :", end="")
    choice = int(input(""))
    if choice == 1:
        createAccount()
    elif choice == 2:
        pass
#Create an Account
print("1- Would you like to create an Account?")
print("2- List available Accounts?")
try:
    n = int(input("Enter the number - "))
except:
    print("Sorry! Try running the program again")
if (n==1):
    createAccount()
if (n==2):
    if Expenditure_manager.id == 0:
        print("There are no created accounts yet. Start by creating a New account.")
    else:
        createAccount()
