#OOP PART

ACCOUNTS = [None] #Approach to create dynamic new accounts and storing it in chadgpt
sendtoBuffer = []
class NotenoughAcct(Exception): #raise an Exception when you dont have enough Accounts
    pass
class NotEnoughMoney(Exception): #raise an Exception when you dont have enough Monkey
    pass
class Expenditure_manager():
    id = 0
    
    def __init__(self, name:str, iAmount:int, daficit=0):
        self.name = name
        self.balance = iAmount
        self.daficit = daficit
        Expenditure_manager.id +=1
        self.id = Expenditure_manager.id
    # def getCounter(self): #counts the number of users 
    #     return self.counter
    def getName(self):
        return self.name
    def addmoney(self, amount):
        self.balance = self.balance + amount
        print(f"{amount} was added to '{self.name}'")
    def takemoney(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            print("Withdrawal Complete.")
            print(f"Current balance in '{self.name}' is {self.balance}")
        else:
            print(f'\n Withdraw interrupted, Not enough balance')
    def makedaficit(self, amount, acc):
        acc.daficit = acc.daficit + amount
        print(f"{acc.name} owes {amount} to {self.name}")
    def trans(self, i, amount, length): #self, account, amount_to_deficit, len of sent_to_list

        try:
            i.addmoney(amount/length)
            self.makedaficit(amount, i)
            self.takemoney(amount)
            print("Transaction completed!")
        except NotEnoughMoney:
            print("Not enough Money!")
        
    #now I have to create a send money feature
    #for that I need a deposite, withdrawal and transaction feature
    #and I need to create a function which confirms wheather and transaction is viable or not
    #also a feature which can confirm wheather there are enough accounts to do a transc
    
###############################
###############################
###############################
 
### # # ### ### ##  # #### I ### #  # #### ###
##   #  ### ##  # # # #  # I  #  #  # # ## ##
### # # #   ### #  ## #### I  #  #### #  # ###

###############################
###############################
###############################

print("Welcome to the Expenditure manager!")
def createAccount(): #Logic to create an Account
    flag = 1
    while flag!=0:
        print("Great! What's the name of the Account? : ", end="")
        name = str(input(""))
        print("What's the initial Balance in the Account? : ", end="")
        balance = int(input(""))
        newaccount = Expenditure_manager(name, balance)
        ACCOUNTS.insert(newaccount.id, newaccount)
        
        print(f"New Account '{name}' created' with ID {newaccount.id} and balance: {newaccount.balance:.2f}")
        a = str(input("Do you wish to add more? (y.n): "))
        if a == 'n':
            print("\n*****ACCOUNT(s) CREATED*****")
            for i in range(1,len(ACCOUNTS)):
                print(f"\nName: {ACCOUNTS[i].name}, ID: {ACCOUNTS[i].id}, Amount: {ACCOUNTS[i].balance}") #Printing the list of currently made accounts
            flag = 0
            proceed()
        else:
            continue
def accountstorecieve(sender):
    global flagchoice
    flagchoice=1
    while flagchoice==1:
        print("Who is reciveing the money? : ")
        rec = int(input())
        if (ACCOUNTS[rec] in sendtoBuffer) or ACCOUNTS[rec]==sender:
            print(f"Element with ID {rec} already chosen.\nYou may choose another account.")
        else:
            sendtoBuffer.append(ACCOUNTS[rec])
        print("Add money to more accounts? (y/n): ")
        moreacc = str(input(""))

        if moreacc == 'y':
            accountstorecieve()
        else:
            flagchoice=0
def proceed(): # What to do AFTER an Account is created
    print("What do you wish to do?")
    print("1- Create another account? :", end="")
    print("\n")
    print("2- Do an expenditure? :", end="")
    choice = int(input(""))
    if choice == 1:
        createAccount()
    elif choice == 2:
        print("\nDoing a Transaction..")
        flagchoice = 0
        print("ID of the person who is giving the money? : ", end='')
        sender = int(input())
        print("How much money do you wish to expend? ")
        money = int(input())
        accountstorecieve(sender)
        a = money/len(sendtoBuffer)
        for i in sendtoBuffer:
            # ACCOUNTS[sender].trans(i, money, len(sendtoBuffer))
            ACCOUNTS[sender].takemoney(a)
            if ACCOUNTS[sender].balance>=money:
                i.addmoney(money/len(sendtoBuffer))
                ACCOUNTS[sender].makedaficit(a, i)
            else:
                print(f"Sorry, {ACCOUNTS[sender].name} does not have enough Balance to proceed the transaction! ")
                break
        for i in range(1,len(ACCOUNTS)):
            print(f"\nName: {ACCOUNTS[i].name}, ID: {ACCOUNTS[i].id}, Amount: {ACCOUNTS[i].balance}") #Printing the list of currently made accounts
        print("Now, ", end='')
        proceed()
        # try:
        #     i.addmoney(amount/length)
        #     self.makedaficit(amount, i)
        #     self.takemoney(amount)
        #     print("Transaction completed!")
        # except NotEnoughMoney:
        #     print("Not enough Money!")
# BASIC CODE FLOW
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