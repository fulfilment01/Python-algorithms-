"""You are a school app developer, your employer wants a programme for their students registration and exam portal. Respond to your employer with an algorithm that allows registration, allows users authentication, and allows students to write exam, when they are done with the exam, their score should be updated in their database, when they are done with the exam, they should be able to login again to check their admission status. If the score  is greater than or equals 60, they should be given admission. Else no admission.
On the admission letter, the following information are important: applicant name, address, state of origin, course of study, matric number, duration of course. At the end of the letter, name of the school Registrer should be included """
import random
import time
import mysql.connector as connection
conn = connection.connect(host = "127.0.0.1", user = "root", password = "Owolabi3498$", database = "addmission")
cursor = conn.cursor()

class addmission:
    def __init__(self):
        self.courses = ["EVN", "BCH", "UI/UX", "MCB", "AI"]
        self.registrer = "Mr Ola Aina"
        print("Welcome to Coledge of SQI")
        self.escore = "null"
        self.homepage()

    def homepage(self):
        self.choice = input("Enter 1 to Register for Addmission\nEnter 2 to Login to take Addmission Exam\n: ")
        if self.choice == "1":
            self.reg()
        elif self.choice == "2":
            self.login()
        else:
            print("invalid input")
            SystemExit

    def reg(self):
        self.name = input("Enter your full name\n: ").title()
        self.password = input("Enter your password\n: ")
        self.jambreg = input("Enter your jamb_reg_no\n: ")
        self.address = input("Enter your address\n: ")
        self.origin = input("Enter your State of Origin\n: ").title()
        self.phone_num = input("Enter your phone number\n: ")
        self.regquerry = "insert into addmission_reg(jamb_reg, applicant_name, phone_num, address, pwd, state_of_origin, exam_score, addmission_status, course_of_study, duration, matric_number) values(%s, %s, %s, %s, %s, %s, null, null, null, null, null)"
        self.regval = (self.jambreg, self.name, self.phone_num, self.address, self.password, self.origin)
        cursor.execute(self.regquerry, self.regval)
        conn.commit()
        time.sleep(2)
        print(f"{self.name}\nCongratulations, Your Registration Was Successful 👍🤝")
        time.sleep(2)
        self.homepage()

    def login(self):
        self.password = input("Enter your password\n: ")
        self.jambreg = input("Enter your jamb registration number\n: ")
        self.loginquerry = "select * from addmission_reg where jamb_reg = %s and pwd = %s"
        self.loginval = (self.jambreg, self.password)
        cursor.execute(self.loginquerry, self.loginval)
        self.loginresult = cursor.fetchone()
        while self.loginresult is None:
            print("invalid login")
            self.login()
        else:
            print(f"you've successfully login {self.loginresult[1]}")
            self.operation()

    def operation(self):
        self.op = input("Enter 1 to take addmission Exam\nEnter 2 to check addmission status\n: ")
        if self.op == "1":
            self.exam()
        elif self.op =="2":
            self.status()
        else:
            print("invalid input")
            time.sleep(1)
            self.homepage()

    def exam(self):
        if self.loginresult[6] != None:
            print("you've already taken your addmission exam\nyou are only allowed to check addmission status")
            self.operation()
        else:
            self.nt = 0
            self.score = 0
            self.question = ["where is SQI located in Dugbe?", "SQI is which type of school?",
                    "who is the president of Nigeria?", "which country won the last world cup?", "who is the senate president of Nigeria?"]
            self.options = ["a. Heritage mall\nb. Central bank\nc. Cocoa House", 
                        "a. coding school\nb. business school\nc. fashon school", 
                        "a. perter obi\nb. tinubu\nc. atiku",
                        "a. Agentina\nb. France\nc. Nigeria",
                        "a. akpabio\nb. saraki\nc. mark"]
            self.answer = ["a", "a", "c", "a", "b"]
            for each in self.question:
                print(each)
                time.sleep(2)
                print(self.options[self.nt])
                self.ans = input("Enter your answer: ").strip().lower()
                self.an = self.answer[self.nt]
                if self.ans == self.an:
                    self.score += 20
                else:
                    self.score -= 5
                self.nt += 1
                time.sleep(2)
            print(f"{self.loginresult[1]} your total score is {self.score}")
            self.examquerry = "update addmission_reg set exam_score = %s where jamb_reg = %s"
            self.examval = (self.score, self.jambreg)
            cursor.execute(self.examquerry, self.examval)
            conn.commit()
            self.operation()

    def status(self):
        self.loginresult
        if self.loginresult[6] >= 60:
            self.adm_status = "Addmitted"
            self.duration = "4yrs"
            self.cstd = "EVN"
            self.matric = int(random.randint(10290, 20290))
        elif self.loginresult[6] >= 65:
            self.adm_status = "Addmitted"
            self.duration = "4yrs"
            self.cstd = "UI/UX"
            self.matric = int(random.randint(10290, 20290))
        elif self.loginresult[6] >= 70:
            self.adm_status = "Addmitted"
            self.duration = "4yrs"
            self.cstd = "BCH"
            self.matric = int(random.randint(10290, 20290))
        elif self.loginresult[6] >= 75:
            self.adm_status = "Addmitted"
            self.duration = "4yrs"
            self.cstd = "AI"
            self.matric = int(random.randint(10290, 20290))
        else:
            self.adm_status = "Not Addmitted"
            self.duration = "null"
            self.cstd = "null"
            self.matric = "null"
        self.statusquerry = f"update addmission_reg set addmission_status = {'%s'}, course_of_study = {'%s'}, duration = {'%s'}, matric_number = {'%s'} where jamb_reg = {'%s'}"
        self.statusval = (self.adm_status, self.cstd, self.duration, self.matric, self.loginresult[0])
        cursor.execute(self.statusquerry, self.statusval)
        conn.commit()
        print(f"Addmmission letter.\nAdmission status is: {self.adm_status}\nName: {self.loginresult[1]}\nwith the address: {self.loginresult[3]}\nfrom: {self.loginresult[5]}\nAddmitted into: {self.cstd} department\nwith matric_no: {self.matric}.\nDuration: {self.duration}")
        self.homepage()
addmission()