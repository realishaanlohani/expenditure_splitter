
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
    