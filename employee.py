"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name,monthly,hourly,commission,bonusCommission):
        self.name = name
        self.monthly = monthly
        self.hourly = hourly
        self.commission = commission
        self.bonusCommission = bonusCommission

    def get_pay(self):
        salary = 0

        #calculate the wage 
        if(self.monthly != None):
            salary = self.monthly
        else: 
            salary = self.hourly[0]*self.hourly[1]


        #calculate their bonus 
        if(self.commission != None):
            salary = salary + (self.commission[0]*self.commission[1])
        elif(self.bonusCommission != None ):
            salary = salary + self.bonusCommission

        return salary

    def __str__(self):
        contract_type = ""
        stringPay = ""
        totalPay = f"Their total pay is {self.get_pay()}."



        if(self.recieveCommission() == False):
            if(self.monthly != None and self.recieveCommission() == False ):
                contract_type = "monthly salary"
                stringPay = f"{self.name} works on a {contract_type} of {self.monthly}. "
            else:
                contract_type = "contract"
                stringPay = f"{self.name} works on a {contract_type} of {self.hourly[0]} hours at {self.hourly[1]}/hour. "
        else:
            if(self.bonusCommission != None and self.hourly != None):
                stringPay = f"{self.name} works on a contract of {self.hourly[0]} hours at {self.hourly[1]}/hour and receives a bonus commission of {self.bonusCommission}. "
            elif(self.bonusCommission != None and self.monthly != None):
                stringPay = stringPay = f"{self.name} works on a monthly salary of {self.monthly} and receives a bonus commission of {self.bonusCommission}. " 
            elif(self.commission != None and self.hourly != None):
                stringPay = f"{self.name} works on a contract of {self.hourly[0]} hours at {self.hourly[1]}/hour and receives a commission for {self.commission[0]} contract(s) at {self.commission[1]}/contract. "
            elif(self.commission != None and self.monthly != None):
                stringPay = stringPay = f"{self.name} works on a monthly salary of {self.monthly} and receives a commission for {self.commission[0]} contract(s) at {self.commission[1]}/contract. " 


        
        returnString = f"{stringPay}{totalPay}"

        print(returnString)
        return (returnString)
    
    def recieveCommission(self):
        receives = True
        if(self.commission == None and self.bonusCommission ==None):
            receives = False
        return receives
    
    






# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',4000,None,None,None)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',None,[100,25],None,None)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',3000,None,[4,200],None)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',None,[150,25],[3,220],None)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',2000,None,None,1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',None,[120,30],None,600)
