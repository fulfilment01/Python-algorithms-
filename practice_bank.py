import random
import mysql.connector as connection
conn = connection.connect(host = "127.0.0.1", user = "root", password = "Owolabi3498$", database = "bank")
cursor = conn.cursor()

class Bank:
    def __init__(self):
        print("Welcome here")
        self.regbanks = ["access", "polaris", "gtb"]
        self.homepage()

    def homepage(self):
        choice = input("Enter 1 to login, 2 to register, 3 to deposit ")
        if choice == "1":
            self.login()
        elif choice == "2":
            self.register()
        elif choice == "3":
            self.deposit()
    
    def register(self):
        self.user_bank = input(f'Select one of the following banks\n {self.regbanks} to register: ').lower()
        if self.user_bank in self.regbanks:
            self.name = input('Enter your full name ')
            self.phone = input("Enter your phone number ")
            while len(self.phone) != 11:
                print("Phone number has to be 11 digits")
                self.phone = input("Enter your phone number ")
            self.passw = input("Enter your password ")
            self.c_id = random.randrange(1234567, 7654321)
            self.acct = self.phone[1:]
            self.bal = 0
            self.reg_in_database = f"insert into {self.user_bank} (customer_id, FullName, Phone_Number, Account_Number, Passw, Account_Bal) values({'%s'}, {'%s'}, {'%s'}, {'%s'}, {'%s'}, {'%s'}) "
            self.insert = (self.c_id, self.name, self.phone, self.acct, self.passw, self.bal)
            cursor.execute(self.reg_in_database, self.insert)
            conn.commit()
            print(f"registration successful and your account number is {self.acct}")
            self.login()
        else:
            print("That bank is not registered with us. Go home")
            self.homepage()

    def login(self):
        self.user_bank = input(f'which of the following banks\n{self.regbanks}\nwant to login into: ').lower()
        if self.user_bank in self.regbanks:
            self.user_acc = input("enter your account number: ")
            self.user_passw = input("enter your password: ")
            self.logquery = f"select * from {self.user_bank} where Account_Number = {'%s'} and Passw = {'%s'}"
            self.logval = (self.user_acc, self.user_passw)
            cursor.execute(self.logquery, self.logval)
            self.result = cursor.fetchone()
            if self.result is not None:
                print("login successfull ")
                self.operation()
            else:
                print("invalid login details")
                self.decide = input("enter 1 to register or any other number to login: ")
                if self.decide == "1":
                    self.register()
                else:
                    self.login()
        else:
            print("bank not available try again")

    def operation(self):
        self.user_ch = input(f"welcome to {self.user_bank} which operation will you like to perform.\n enter 1 to transfer\n ")
        if self.user_ch == "1":
            self.transfer()

    def transfer(self):
        self.logquery = f"select * from {self.user_bank} where Account_Number = {'%s'} and Passw = {'%s'}"
        self.logval = (self.user_acc, self.user_passw)
        cursor.execute(self.logquery, self.logval)
        self.result = cursor.fetchone()
        self.recp_bank = input(f"this are the banks you can transfer to {self.regbanks} choose one: ")
        if self. recp_bank in self.regbanks:
            self.rec_acc = input("enter the account number you want to transfer to: ")
            self.recquery = f"select * from {self.recp_bank} where Account_Number = {'%s'}"
            self.recval = (self.rec_acc, )
            cursor.execute(self.recquery, self.recval)
            self.rec_result = cursor.fetchone
            if self.rec_acc is not None:
                self.amount = int(input("enter the amount you want to send: "))
                while self.amount >= self.result[5]:
                    print("insurficient fund")
                    self.amount = int(input("enter the amount you want to send"))
                else:
                    self.new_balance = self.result[5] - self.amount # to deduct from the user account balance
                    self.updatequery = f"update{self.user_bank} set Account_Bal = {'%s'} where Account_Number = {'%s'}"
                    self.upval = (self.new_balance, self.result[3])
                    cursor.execute(self.updatequery, self.upval)
                    conn.commit()
                    self.newrecbal = self.rec_result[5] + self.amount
                    self.updaterecquery = f"update {self.recp_bank} set Account_Bal = {'%s'} where Account_Number = {'%s'}"
                    self.updaterecval = (self.newrecbal, self.rec_acc)
                    cursor.execute(self.updaterecquery, self.updaterecval)
                    conn.commit()
                    print("transfer successful")
            else:
                print("invalid account number")
                self.transfer()
        else:
            print("you dont have a bank registered with us")
            self.transfer()

    def deposit(self):
        self.dep_ch = input(f"welcome\nwhich of the following banks will you like to make deposit\n{self.regbanks}: ")
        if self.dep_ch in self.regbanks:
            self.dep_acc = input("enter the account number you want to deposit money into: ")
            self.dep_accquery = f"select * from {self.dep_ch} where Account_Number = {'%s'}"
            self.dep_accval = (self.dep_acc, )
            cursor.execute(self.dep_accquery, self.dep_accval)
            self.depaccresult =cursor.fetchone()
            if self.depaccresult is not None:
                self.depamount = int(input("enter the amount you want to do deposit: ")) #deposit amount
                print(f"you are about to send money to {self.depaccresult[1]}")
                self.pro = input("enter yes to proceed")
                if self.pro == "yes":
                    self.new_bal = self.depaccresult[5] + self.depamount # adding the deposit aamount to the account balance fetched at the index of 5
                    self.updatedepquery = f"update {self.dep_ch} set Account_Bal = {'%s'} where Account_Number = {'%s'}" # querry for the amount you want to deposit by updating the database
                    self.updatedepval = (self.new_bal, self.dep_acc)
                    cursor.execute(self.updatedepquery, self.updatedepval)
                    conn.commit()
                    print("deposit successful")
                else:
                    print("it seems you are not ready to proceed")
                    self.deposit()
            else:
                print("invalid account number")
                self.homepage()

        else:
            print("the bank you entered is not registered with us")
            self.homepage()

Bank()