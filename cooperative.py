"""
See yourself as a developer of a cooperative society where there can be members and non-members. Members are the people that belong to the cooperative society (those with contribution).
Non-members are those who do not belong to the society but can borrow loans. 
They should be able to borrow and pay-back loans.
When non-members borrow a loan, the interest should be 10%,
For members with no contribution interest should be 7% while members with
contributions interest should be 3%.
Members should be able to contribute.
Whenever a member contributes to the organization they should have an interest of 1% (when u make a contribution whatever your balance is 1% of it should be added). 
We should also keep track of the money in and money out and they should keep them as an organization treasury.
And it's from the treasury the money would be borrowed and kept.
"""
import random
import datetime
import time
import mysql.connector as connection
conn = connection.connect(host = "127.0.0.1", user = "root", password = "Owolabi3498$", database = "cooperative")
cursor = conn.cursor()

class cooperative:
    def __init__(self):
        print("you are welcome to SQI co-operative society")
        self.status= "not login"
        self.homepage()

    def homepage(self):
        self.opp=input("Enter 1 to register as a member\nEnter 2 to apply for loan\nEnter 3 to make contributions\nEnter 4 to pay back your loan\n: ")
        if self.opp=="1":
            self.register()
        elif self.opp=="2":
            self.apply4loan()
        elif self.opp=="3":
            self.contribution()
        elif self.opp=="4":
            self.pay_loan()
        else:
            SystemExit

    def register(self):#this is a registration function where non memebers can register and a member can not register twice 
        self.name=input("Enter your full name\n: ").title()
        self.phonenumber=input("Enter your phone number\n: ")
        while len(self.phonenumber) != 11 :
            print("invalid phone number")
            self.phonenumber=input("Enter your phone number\n: ")
        else:
            self.address=input("Enter your address\n: ").title()
            self.state_of_origin=input("Enter your state of origin\n: ").title()
            self.user=input("Enter your username\n: ")
            self.pwd=input("Enter your password\n: ")
            self.member_id= "SQI" + str(random.randrange(100, 200))
            self.amtcon= 0
            self.amtbor= 0
            self.con_intre= 0
            self.borrowed_int= 0
            self.querry= "insert into members_table(member_id, full_name, phone_num, address, username, pwd, state_of_origin, amount_contributed, amount_borrowed, cont_interest_rate, loan_interest_rate) values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            self.val=(self.member_id, self.name, self.phonenumber, self.address, self.user, self.pwd, self.state_of_origin, self.amtcon, self.amtbor, self.con_intre, self.borrowed_int)
            cursor.execute(self.querry, self.val)
            conn.commit()
            time.sleep(2)
            print(f"{self.name}, you have successfully registered as a member")
            self.homepage()

    def contribution(self):
        print("Please login to make contribution")
        time.sleep(1)
        self.usern=input("Enter your username\n: ")
        self.passw=input("Enter your password\n: ")
        self.querry= "select * from members_table where username = %s and pwd = %s"
        self.vall=(self.usern, self.passw)
        cursor.execute(self.querry, self.vall)
        self.loginresult = cursor.fetchone()
        while self.loginresult is None:
            print("Invalid login")
            self.homepage()
        else:
            time.sleep(2)
            print(f"{self.loginresult[1]}, you've successfully logged in\nkindly proceed to make your contribution")
            self.transid=random.randrange(12321, 23212)
            self.nam=self.loginresult[1]
            self.date= datetime.date.today()
            print()
            self.contribute= int(input("Enter the amount you want to contribute\n: "))
            self.con_interest= 0.01 * self.contribute
            self.con= self.contribute + self.con_interest
            self.bal= self.loginresult[7] + self.con
            self.conquerry= "update members_table set amount_contributed = %s, cont_interest_rate = %s where phone_num = %s"
            self.convall= (self.bal, self.loginresult[2])
            cursor.execute(self.conquerry, self.convall)
            conn.commit()
            self.transquerry= "insert into treasurers_cr_acc(transaction_id, full_name, amount_paid_in, dates) values(%s, %s, %s, %s)"
            self.transvall= (self.transid, self.nam, self.contribute, self.date)
            cursor.execute(self.transquerry, self.transvall)
            conn.commit()
            print(f"{self.loginresult[1]}\nYou've successfully made your contribution")
cooperative()