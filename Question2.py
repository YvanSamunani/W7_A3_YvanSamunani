import random
import sys
from datetime import datetime
from datetime import timedelta


class DangoteBank():
    def __init__(self, name, acc_num, acc_pin):
        self.name = name
        self.acc_num = acc_num
        self.acc_pin = acc_pin
        self.balance = 0
        self.savings = 0
        self.current = 0

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)

    def saving_acc(self):
        print("For a saving account, the interest is 3% withdrawn after 6 months.")
        saved_cash = float(input("Enter amount to be saved: "))
        interest = (saved_cash * 6) / 100
        self.savings = saved_cash + interest

    def current_acc(self):
        print("For a current account, the interest is 1%.")
        current_cash = float(input("Enter amount to be saved: "))
        interest = (current_cash * 1) / 100
        self.current = current_cash + interest

    def withdraw_savings(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.savings >= amount:
            self.savings -= amount
            print("\n You Withdrew:", amount)

        else:
            print("\n Insufficient balance ")

    def withdraw_current(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.current >= amount:
            self.current -= amount
            print("\n You Withdrew:", amount)

        else:
            print("\n Insufficient balance ")

    def transfer_savings(self):

        trans_amount = float(input("How much would you like to transfer: "))
        trans_account = input("Transfer to which account: ")
        if self.savings > trans_amount:
            self.savings -= trans_amount
            print("\n You have transferred:", trans_amount, " to this account: ", trans_account)
        else:
            print("\n Insufficient balance ")

    def transfer_current(self):

        trans_amount = float(input("How much would you like to transfer: "))
        trans_account = input("Transfer to which account: ")
        if self.current > trans_amount:
            self.current -= trans_amount
            print("\n You have transferred:", trans_amount, " to this account: ", trans_account)
        else:
            print("\n Insufficient balance ")

    def display_savings(self):

        print("\n Net Available Balance=", self.savings)

    def display_current(self):

        print("\n Net Available Balance=", self.current)


print("Hello!!! Welcome to Dangote Bank \nPlease create an account to access our services: ")


def main():
    global na
    global ac_num
    global ca_pin
    global s
    global create_acc

    create_acc = int(input("1) Saving Account\n2) Current Account: "))

    if create_acc == 1:

        na = input("Enter your name: ")
        ac_num = random.randint(100000000000, 999999999999)
        ca_pin = random.randint(1000, 9999)
        Begindatestring = "2021-11-11"
        Begindate = datetime.strptime(Begindatestring, "%Y-%m-%d")
        print("Your account has been successfully created on" , Begindate)
        print("Name: ", na, "\n", "Account Number: ", ac_num, "\n", "Card Pin: ", ca_pin, "\n")
        Enddate = Begindate + timedelta(days=150)
        print("You will be able to withdraw starting from: ", Enddate)
        s = DangoteBank(na, ac_num, ca_pin)
        option = input("Would you like to continue with our services? [Y/N]:  ")
        if option == "Y" or option == "y":
            bank_service()

        else:
            pass

    if create_acc == 2:

        na = input("Enter your name: ")
        ac_num = random.randint(100000000000, 999999999999)
        ca_pin = random.randint(1000, 9999)
        print("Your account has been successfully created: ")
        print("Name: ", na, "\n", "Account Number: ", ac_num, "\n", "Card Pin: ", ca_pin, "\n")
        s = DangoteBank(na, ac_num, ca_pin)
        option = input("Would you like to continue with our services? [Y/N]:  ")
        if option == "Y" or option == "y":
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
        if create_acc == 1:
            s.saving_acc()
            s.display_savings()
            option = input("Would you like to continue with our services? [Y/N]:  ")
            if option == "Y" or option == "y":
                bank_service()

            if option == "n" or option == "N":
                print("\nThank you for using Dangote Bank")

                sys.exit()

        if create_acc == 2:
            s.current_acc()
            s.display_current()
        option = input("Would you like to continue with our services? [Y/N]:  ")
        if option == "Y" or option == "y":
            bank_service()

        if option == "n" or option == "N":
            print("\nThank you for using Dangote Bank")

            sys.exit()

    if service == 2:
        if create_acc == 1:
            s.withdraw_savings()
            s.display_savings()
            option = input("Would you like to continue with our services? [Y/N]:  ")
            if option == "Y" or option == "y":
                bank_service()

            if option == "n" or option == "N":
                print("\nThank you for using Dangote Bank")
                sys.exit()
        if create_acc == 2:
            s.withdraw_current()
            s.display_current()
            option = input("Would you like to continue with our services? [Y/N]:  ")
            if option == "Y" or option == "y":
                bank_service()

            if option == "n" or option == "N":
                print("\nThank you for using Dangote Bank")
                sys.exit()

    if service == 3:
        if create_acc == 1:
            s.transfer_savings()
            s.display_savings()
            option = input("Would you like to continue with our services? [Y/N]:  ")
            if option == "Y" or option == "y":
                bank_service()

            if option == "n" or option == "N":
                print("\nThank you for using Dangote Bank")

                sys.exit()

        if create_acc == 2:
            s.transfer_current()
            s.display_current()
            option = input("Would you like to continue with our services? [Y/N]:  ")
            if option == "Y" or option == "y":
                bank_service()

            if option == "n" or option == "N":
                print("\nThank you for using Dangote Bank")

                sys.exit()

    if service == 4:
        if create_acc == 1:
            s.display_savings()
            option = input("Would you like to continue with our services? [Y/N]:  ")
            if option == "Y" or option == "y":
                bank_service()

            if option == "n" or option == "N":
                print("\nThank you for using Dangote Bank!")
                sys.exit()

        if create_acc == 2:
            s.display_current()
            option = input("Would you like to continue with our services? [Y/N]:  ")
            if option == "Y" or option == "y":
                bank_service()

            if option == "n" or option == "N":
                print("\nThank you for using Dangote Bank!")
                sys.exit()

main()