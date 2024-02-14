"""A simple program to ask food seller the food and protein she has,
if her food is rice and her protein is egg, tell the seller that you will buy rice and egg,
else, you will not buy anything"""

# val1 = str(input("Which food is availabel ? : ")).strip().lower() 
# val2 = str(input("Which of the protein is available ? :  "))

# food = "rice"
# protein = "egg"

# if val1 == food and val2 == protein :
#     print('i want to buy rice and egg')
# else:
#      print('i will not buy anything')
import time
class food:
    def __init__(self):
        self.protein = ["Egg", "beaf", "ogunfe", "chicken", "fish", "bokoto", "ponmon", "inu eran", "gizzard"]
        self.food = ["rice", "beans", "amala", "pounded yam", "eba"]
        self.soup = ["egusi soup", "ewedu soup", "bitter_leave soup", "okro soup", "ogbonno soup", "stew"]
        self.operation()

    def operation(self):
        self.choose = input("Enter 1 to choose your menu\nEnter any key to Exit")
        while self.choose != "1":
            SystemExit
        else:
            self.choice()

    def choice(self):
        val1 = input(f"which food will you like to eat from\n{self.food}\n: ")
        time.sleep(2)
        val2 = input(f"which soup will you like to add to your food\n{self.soup}\n: ")
        while val1 in self.food and val2 in self.soup:
            time.sleep(2)
            val3 = input(f"which protein will you like to add\n{self.protein}\n: ")
            if val3 in self.protein:
                print(f"your order is available\n\n{val1}\n\n{val2}\n\n{val3}")
                self.operation()
            else:
                print("your order is not available")
                self.operation()
        else:
            print("your order is not available")
            self.operation()
food()