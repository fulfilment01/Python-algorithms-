"""create a school score grading app that will have CA1, CA2 and Exam,
if  the score is 75 and above grade the person A. if the score is 60 but less than
75 grade should be B, if the score is 50 but les than 60, grade should be C,
If the score is  40 but less than 50, grade should be D, if the score is below 40, grade should be F """

import time
class CA:
    def __init__(self):
        print("this program is used for computation")
        A = 5.0
        B = 4.0
        C = 3.0
        D = 2.0
        E = 1.0
        F = 0
        time.sleep(1)
        self.CA()

    def CA(self):
        self.ca1 = float(input("Enter CA1: "))
        self.ca2 = float(input("Enter CA2: "))
        self.Exam = float(input("Enter Exam score: "))
        self.ca3 = float((self.ca1 + self.ca2) / 2)
        self.total_score = self.Exam + self.ca3
        if self.ca3 <= 30 and self.total_score <= 100:
            time.sleep(1)
            print(self.total_score)
            time.sleep(1)
            if self.total_score >= 75:
                print("Grade= A")
            elif self.total_score >= 60:
                print("Grade= B")
            elif self.total_score >= 50:
                print("Grade= C")
            elif self.total_score >= 40:
                print("Grade= D") 
            else:
                print("Grade= F")
        else: 
            print("error")
CA()