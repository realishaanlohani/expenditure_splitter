import csv
ACCOUNTS = [None]
class Person():
    id = 0
    def __init__(self, name: str, debt=0):
        self.name = name
        self.balance = 0
        self.debt = debt  
        Person.id += 1
        self.id = Person.id
    def adddebt(self, person , amount):
        person.debt += amount  # Add money to the balance
        self.debt -= amount
        if (person.name!=self.name):
            print(f"{person.name} owes ${amount/len(sendtobuffer)} to '{self.name}'")

class Expense():
    def __init__(self, paid_by:str, amount:int, participants:list):
        self.payer = paid_by
        self.amount = amount
        
class ExpenseManager():
    def __init__(self, listofpeeps:list, listofexpense:list): #this is defined in each transaction
        pass
print("-----WELCOME TO THE XPENDITURE MANAGER\n Kindly pick one of the multipe options\n")

def seestatus():

    for i in range(1, len(ACCOUNTS)):
        print(f"Name: {ACCOUNTS[i].name}, ID: {ACCOUNTS[i].id}, Debt: {ACCOUNTS[i].debt}")

def main():
    try:
        while True:
            print("\n1- Add a new person")
            print("2- Make an Expenditure")
            print("3- Check transaction histrory.")
            print("0- Exit: ")

            choice = int(input("\nEnter your choice - "))

            if choice == 1:
                name = str(input("Enter name of the Account - "))
                newacc = Person(name)
                ACCOUNTS.append(newacc)
                print("\n" + newacc.name + " added to the ACCOUNTS list\n")
                print("\n***Currently added accounts***\n")
                seestatus()
            if choice==2:
                global sendtobuffer
                sendtobuffer =[]
                sendtobuffernames = []
                print("\nDoing a transaction...\n")
                whoispaying = int(input("\nWho is paying? (Enter the ID only): "))
                # amountpayed = input("Amount payed? : ")
                stringcarryingparties = list(input("Enter the ids of accounts, separated by spaces: ").split())
                # listofvbalidids = []

                # for i in range(1, len(ACCOUNTS)):
                #     listofvbalidids.append(ACCOUNTS[i].id)
                # for i in stringcarryingparties:
                #     if i not in listofvbalidids:
                #         print("Not valid")
                        # continue

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

                print("\nRepititions would be cleared!!\n")
                amountpaid = int(input("Enter the amount payed : "))

                for i in stringcarryingparties:
                    sendtobuffer.append(ACCOUNTS[int(i)])
                    sendtobuffer= list(set(sendtobuffer+[ACCOUNTS[whoispaying]]))

                for i in sendtobuffer:
                    sendtobuffernames.append(i.name)

                purpose = input("Payed for?: ")
                with open("bigo.csv", "a+") as file:
                    writer = csv.writer(file)
                    writer.writerow([f'{ACCOUNTS[whoispaying].name}', f'{amountpaid}', f'{purpose}', f'{sendtobuffernames}']) 
                print(sendtobuffer)
                for sec in sendtobuffer:
                    if ACCOUNTS[whoispaying]!= sec.id:
                        ACCOUNTS[whoispaying].adddebt(sec, amountpaid)
                        with open("owes_record.csv", "a+") as file:
                            
                
            if choice==3:
                with open("bigo.csv", "r") as readfile:
                    reader = csv.reader(readfile)
                    for line in reader:
                        print(f"{line[0]} payed {line[1]} for {line[2]} spilt equally among {"".join(line[3].strip('[],'))}")
            if choice==0:
                exit()
    except ValueError:
        main()
main()
