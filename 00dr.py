class Account:
    def __init__(self, id, balance, interestRate):
        self.__id = id
        self.__balance = balance
        self.__interestRate = interestRate

    def getID(self):
        return self.__id

    def getBalance(self):
        return self.__balance

    def getInterestRate(self):
        return self.__interestRate

    def getmonthlyintereserate(self):
        return self.__interestRate/12

    def checkbalance(self):
        return self.__balance

    def deposite(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        self.__balance -= amount


acc1 = Account(1, 100, 4)
# if(acc1.__balance == 1):
#     print("Yes")
acc2 = Account(2, 100, 4)
acc3 = Account(3, 100, 4)
acc4 = Account(4, 100, 4)
acc5 = Account(5, 100, 4)
acc6 = Account(6, 100, 4)
acc7 = Account(7, 100, 4)
acc8 = Account(8, 100, 4)
acc9 = Account(9, 100, 4)
acc10 = Account(10, 100, 4)
accounts = [acc1, acc2, acc3, acc4, acc5, acc6, acc7, acc8, acc9, acc10]

exit = False

while(exit == False):
    userId = int(input("Enter your ID: "))
    userInfoTrue = False
    userNo = 0
    for i in accounts:
        if(userId == i.__balance):
            userInfoTrue = True
            userNo += 1
            break
    if(userInfoTrue == False):
        print("Invalid user ID")
        break
    print("Hello user " + userNo)
    print("You can go for 4 options")
    choice = int(input(("""
    1. Check Balance
    2. Withdraw
    3. Deposit
    4. Exit
    """)))
    currAccount = accounts[userNo]
    if(choice == 1):
        print(currAccount.checkbalance)
    elif(choice == 2):
        amount = int(input("Enter the amount to be withdrawn: "))
        currAccount.withdraw(amount)
        print("Amount successfully withdrawn!!!")
    elif(choice == 3):
        amount = int(input("Enter the amount to be deposit: "))
        currAccount.deposite(amount)
        print("Amount successfully deposited!!!")
    elif(choice == 4):
        print("Thanks for visiting!!!")
        break
    else:
        print("Enter a valid choice between 1 and 4!!!")
