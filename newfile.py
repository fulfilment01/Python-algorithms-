import random
import time
import mysql.connector as connection
conn = connection.connect(host = "127.0.0.1", user = "root", password = "Owolabi3498$", database = "SQI")
cursor = conn.cursor()
class SQI:
    def __init__(self):
        print("Welcome to SQI school of coding")
        self.departments = ["data_science", "data_analysis", "web_development", "javascript", "graphic_design", "cyber_security", "ui_ux"]
        # self.president = ["Bamidele Olaitan", "Akomolede Ileri"]
        # self.vice_president = ["Timilehin Ojo", "Victoria Zillion"]
        # self.gen_sec = ["Terri Renita", "Ini Bode"]
        self.election = ["president", "vice_president", "gen_sec"]
        self.elecCand = {
            "president":["Bamidele Olaitan", "Akomolede Ileri"],
            "vice_president":["Timilehin Ojo", "Victoria Zillion"],
            "gen_sec":["Terri Renita", "Ini Bode"]
        }
        self.homepage()

    def homepage(self):
        self.studentchoice = input("Enter 1 to register\nEnter 2 to login: ")
        if self.studentchoice == "1":
            self.register()
        elif self.studentchoice == "2":
            self.login()
        else:
            print("invalid input")
            SystemExit
    # you haave to register as a student of SQI before you can login, register, and exercise your civic accademic franchise.
    def register(self):
        time.sleep(2)
        self.stdreg = input(f"select one of the following departments\n{self.departments} to register ")#you are to pick out of the available department in the self.departmnets list 
        if self.stdreg in self.departments:
            time.sleep(1)
            self.sur_name = input("Enter your surname: ").title()
            self.first_name = input("Enter your first name: ").title()
            self.matric_no = int(random.randrange(10009, 11111))
            self.level = input("Enter your level: ")
            self.user = input("Enter your username: ")
            self.pwd = input("Enter your password: ")
            self.stdreg_query = f"insert into {self.stdreg} (matric_number, surname, firstname, username, pwd, levels) values({'%s'}, {'%s'}, {'%s'}, {'%s'}, {'%s'}, {'%s'})"# we inserting into the department you choose i.e self.stdreg
            self.inserstdregval = (self.matric_no, self.sur_name, self.first_name, self.user, self.pwd, self.level)
            cursor.execute(self.stdreg_query, self.inserstdregval)
            conn.commit()
            print(f"registration successful\nyour matric_number is:\n{self.matric_no}")
            self.login()
        else:
            time.sleep(1)
            print("the department you entered is not available") 
            self.homepage()

    #you have to login into the school portal as a student in one of the listed department before you can register,cast, and count vote        
    def login(self):
        time.sleep(2)
        self.std = input(f"Enter your department out of the available departments to login\n{self.departments}:\n")
        if self.std in self.departments:
            time.sleep(1)
            self.stdusername = input("Enter your username: ")
            self.stdpwd = input("Enter your password: ")
            self.loginquery = f"select * from {self.std} where username = {'%s'} and pwd = {'%s'}"
            self.loginval = (self.stdusername, self.stdpwd)
            cursor.execute(self.loginquery, self.loginval)
            self.loginresult = cursor.fetchone()
            if self.loginresult is None:
                print("inavlid login")
                self.login()
            else:
                print("login successful")
                self.operation()
        else:
            print("department not available")
            self.homepage()        

    def operation(self):
        time.sleep(1)
        self.std_choice = input("which of the following operation will you like to perform.\nEnter 1 for voting registration\nEnter 2 to cast vote\nEnter 3 to check voting result: ")
        if self.std_choice =="1":
            self.vote_registration()
        elif self.std_choice == "2":
            self.cast_vote()
        elif self.std_choice =="3":
            self.count_vote()
        else:
            print("you can only exercise your civic franchise")
            self.homepage()

    def vote_registration(self):
        self.std_voter_matric = input("Enter your matric number: ")
        self.std_vote_regdept = input("Enter your department: ").lower()
        if self.std_vote_regdept in self.departments:
            self.std_vote_regdep_query = f"select * from {self.std_vote_regdept} where matric_number = {'%s'}"
            self.stdvoteval = (self.std_voter_matric, )
            cursor.execute(self.std_vote_regdep_query, self.stdvoteval)
            self.voteregresult = cursor.fetchone()
            print(self.voteregresult)
            if self.voteregresult is not None:
                self.voters_card = random.randrange(811, 899)
                self.fullname = self.voteregresult[1] + " " + self.voteregresult[2]
                self.levells = self.voteregresult[5]
                self.vote_reg_query = "insert into voting_reg_table (voters_card, matric_number, full_name, department, levels, president, vice_president, gen_sec) values(%s, %s, %s, %s, %s, %s, %s, %s)"
                self.vote_reg_val = (self.voters_card, self.std_voter_matric, self.fullname, self.std_vote_regdept,
                                     self.levells, "nill", "nill", "nill")
                cursor.execute(self.vote_reg_query, self.vote_reg_val)
                conn.commit()
                print(f"registration successful\nyour voters card number is {self.voters_card}")
                self.operation()
        else:
            print("department not found")
            self.homepage()

    def cast_vote(self):
        self.std_voters_card = int(input("Enter your voters card number: "))
        self.cardquerry = "select * from voting_reg_table where voters_card = %s"
        self.cardval = (self.std_voters_card, )
        cursor.execute(self.cardquerry, self.cardval)
        self.card_result = cursor.fetchone()
        print(self.card_result)
        self.voteconfirm()
                   
    def voteconfirm(self):
        if self.card_result is not None:
            self.votechoice = input(f"select from the category of election\n{self.election}:\n>>>")           
            if self.votechoice in self.election:
                if self.votechoice == "president":
                    index = 5
                elif self.votechoice == "vice_president":
                    index = 6
                elif self.votechoice == "gen_sec":
                    index = 7

                if self.card_result[index] != "nill":# this is to make sure a candidate doesnt vote twice 
                    print("You have already voted in this category")
                    inp = input("Enter 1 to vote again or 2 to go back home")
                    if inp == "1":
                        self.voteconfirm()
                    else:
                        self.operation()
                else:
                    print(f"this are the list of the {self.votechoice} candidate\n {self.elecCand[self.votechoice]}")
                    self.vote = input("Enter the name of the candidate you are voting for\n>>> ")
                    while self.vote not in self.elecCand[self.votechoice]:
                        print("Candidate not among")
                        self.vote = input("Enter the name of the candidate you are voting for\n>>> ")
                    else:
                        self.querry = f"update voting_reg_table set {self.votechoice} = {'%s'} where voters_card = {'%s'}"
                        self.val = (self.vote, self.std_voters_card)
                        cursor.execute(self.querry, self.val)
                        conn.commit()
                        print(f"you have successfully voted for {self.vote}")
                        inp = input("Enter 1 to vote again or 2 to go back home")
                        if inp == "1":
                            self.voteconfirm()
                        else:
                            self.operation()
        else:
            print("you have entered an invalid voters_card number")
            time.sleep(1)
            self.vote_registration()

    def count_vote(self):
        self.winner = {}
        self.voteresult = input("Enter 1 to view overall result\nEnter 2 to view of departmental result\n: ")
        if self.voteresult == "1":
            self.resultcategory = input(f"Enter the category you want to view from\n{self.election}\n:").lower()
            while self.resultcategory not in self.election:
                print("category not found")
                self.resultcategory = input(f"Enter the category you want to view from\n{self.election}\n: ").lower()
            else:
                for name in self.elecCand[self.resultcategory]: #the name represents each of the names in the self. election categories. i.e: President can have "Ade, Bade..."
                    self.resultquerry = f"select count({self.resultcategory}) from voting_reg_table where {self.resultcategory} = {'%s'}" #self.resultcategory is the category the user selects i.e president, gensec and others.
                    self.resultval = (name,) #we are trying to insert the name as the value of that %s
                    cursor.execute(self.resultquerry, self.resultval)
                    self.voteregresult = cursor.fetchone()
                    time.sleep(2)
                    print(f"{name} has {self.voteregresult[0]} votes")
                    self.winner.update({name:self.voteregresult[0]})    
                print(f"The winner is {max(self.winner)}")
                self.operation()

        elif self.voteresult == "2":
            self.deptresult = (input(f"select one of the following departments\n{self.departments}\nto view result: "))
            if self.deptresult in self.departments:
                self.resultcategory = input(f"Enter the category you want to view from\n{self.election}\n:").lower()
                while self.resultcategory not in self.election:
                    print("category not found")
                    self.resultcategory = input(f"Enter the category you want to view from\n{self.election}\n:").lower()
                else:
                    for name in self.elecCand[self.resultcategory]: #the name represents each of the names in the self. election categories. i.e: President can have "Ade, Bade..."
                        self.resultquerry = f"select count({self.resultcategory}) from voting_reg_table where {self.resultcategory} = {'%s'} and department = {'%s'}" #self.resultcategory is the category the user selects i.e president, gensec and others.
                        self.resultval = (name, self.deptresult) #we are trying to insert the name as the value of that %s
                        cursor.execute(self.resultquerry, self.resultval)
                        self.voteregresult = cursor.fetchone()
                        time.sleep(2)
                        print(f"{name} has {self.voteregresult[0]} votes in {self.deptresult} department")
                        self.winner.update({name:self.voteregresult[0]})
                    print(f"The winner is {max(self.winner)} in {self.deptresult} department")
                    self.operation()
        else:
            print("you can only check result in this section bitch")
            self.operation()
SQI()
