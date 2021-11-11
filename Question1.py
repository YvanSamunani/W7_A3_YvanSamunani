import random
import sys


class DangoteBank():
    def __init__(self, name, acc_num, acc_pin):
        self.name = name
        self.acc_num = acc_num
        self.acc_pin = acc_pin
        self.balance=0


    def deposit(self):
        amount=float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:",amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance>=amount:
            self.balance-=amount
            print("\n You Withdrew:", amount)

        else:
            print("\n Insufficient balance ")

    def transfer(self):

        trans_amount = float(input("How much would you like to transfer: "))
        trans_account = input("Transfer to which account: ")
        if self.balance > trans_amount:
            self.balance -= trans_amount
            print("\n You have transferred:", trans_amount, " to this account: ", trans_account)
        else:
            print("\n Insufficient balance ")

    def display(self):
        print("\n Net Available Balance=",self.balance)


print("Hello!!! Welcome to Dangote Bank \nPlease create an account to access our services: ")


def main ():
    global na
    global ac_num
    global ca_pin
    global s
    na = input("Enter your name: ")
    ac_num = random.randint(100000000000, 999999999999)
    ca_pin = random.randint(1000, 9999)
    print("Your account has been successfully created:")
    print("Name: ", na, "\n", "Account Number: ", ac_num, "\n", "Card Pin: ", ca_pin, "\n")
    s = DangoteBank(na, ac_num, ca_pin)
    option = input("Would you like to continue with our services? [Y/N]:  ")
    if option == "Y" or option =="y":
        bank_service()

    else:
        pass

def inquiry():

    global service

    service = int(input("1) Deposit" + "\n" + "2) Withdraw" + "\n" + "3) Transfer" + "\n" + "4) Check balance: "))


def bank_service():
    inquiry()
    global s
    if service == 1:
        s.deposit()
        s.display()
        option = input("Would you like to continue with our services? [Y/N]:  ")
        if option == "Y" or option == "y":
            bank_service()

        if option == "n" or option == "N":
            print("\nThank you for using Dangote Bank")

            sys.exit()

    if service == 2:
        s.withdraw()
        s.display()
        option = input("Would you like to continue with our services? [Y/N]:  ")
        if option == "Y" or option == "y":
            bank_service()

        if option == "n" or option == "N":
            print("\nThank you for using Dangote Bank")
            sys.exit()

    if service == 3:
        s.transfer()
        s.display()
        option = input("Would you like to continue with our services? [Y/N]:  ")
        if option == "Y" or option == "y":
            bank_service()

        if option == "n" or option == "N":
            print("\nThank you for using Dangote Bank")

            sys.exit()

    if service == 4:
        s.display()
        option = input("Would you like to continue with our services? [Y/N]:  ")
        if option == "Y" or option == "y":
            bank_service()

        if option == "n" or option == "N":
            print("\nThank you for using Dangote Bank!")
            sys.exit()

main()