"""Create a shopping mall app with 7 different collections. Collection 1: cooking wares,  collection 2: drinks, collection 3: computers, collection 4: toileteries,  collection 5: home appliances, collection 6: fashion(A: Men's wear, B: Women's wear), 
customers can decide to add to cart without opening account but should not be able to pay out without account, or customer should open an account before making purchase.
user should be able to buy from any of the collections they want, when they purchase from a collection, all your sales should be entering sales table."""


import random
import mysql.connector as connection
conn = connection.connect(host = "127.0.0.1", user = "root", password = "Owolabi3498$", database = "shoppingmall")
cursor = conn.cursor()
class Ecommerce:
    def __init__(self):
        print("welcome")
        self.number_of_trials = 0
        self.cart_category = {}
        self.cart_items = {}
        self.price = {}
        self.status = "not login"
        self.collection = ["cooking_wares", "drinks", "computers", "toileteries", "home_appliances", "men's_wears", "women's_wears"]
        self.operations()

    def operations(self):
        self.op = input("Enter 1 to login\nEnter 2 to Register\nEnter 3 to add to cart\nEnter 4 to checkout\n: ")
        if self.op == "1":
            self.login()
        elif self.op == "2":
            self.reg()
        elif self.op == "3":
            self.add_to_cart()
        elif self.op == "4":
            self.checkout()
        else:
            SystemExit

    def add_to_cart(self):
        self.shop = input(f"which of the collections will you like to shop from\n{self.collection}\n: ").lower()
        if self.shop in self.collection:
            self.shopquerry = f"select product_name from {self.shop} "
            cursor.execute(self.shopquerry)
            self.shopresult = cursor.fetchall()
            print(f"this are the product under this collection\n{self.shopresult}")
            self.pick = input("enter the product you wannt to purchase\n: ")
            while (self.pick,) not in self.shopresult:
                print("your pick is not available in this category")
                self.pick = input("enter the product you wannt to purchase\n: ")
            else:
                self.pickquerry = f"select * from {self.shop} where product_name = {'%s'}"
                self.pickval = (self.pick, )
                cursor.execute(self.pickquerry, self.pickval)
                self.pickresult = cursor.fetchone()
                print(f"the curent price of {self.pick}\nis {self.pickresult[2]}\nand there are {self.pickresult[3]} left")
                self.picknum = int(input(f"how many {self.pick} will you like to buy\n: "))
                while self.picknum > self.pickresult[3]:
                    print("out of stock or the required quantity is not available")
                    self.picknum = int(input(f"how many {self.pick} will you like to buy\n: "))
                else:
                    self.p = self.picknum * self.pickresult[2]
                    self.cart_items.update({self.pick:self.picknum})
                    self.price.update({self.pick:self.p})
                    self.cart_category.update({self.shop:self.cart_items})
                    print("you have successfully added the items to your cart")
                    print(self.cart_category)
                    self.chektry = input("Enter 1 to try again\nEnter 2 to checkout: ")
                    if self.chektry == "1":
                        self.add_to_cart()
                    elif self.chektry == "2":
                        self.checkout()
                    else:
                        self.operations()

    def reg(self):
        self.username = input("enter your username: ")
        self.password = input("enter your password: ")      
        self.phone = input("enter your phone number: ")
        while len(self.phone) != 11:
            print("the phone number must be 11 digit")
            self.phone = input("enter your phone number: ")
        self.fullname = input("enter your full name: ").title()
        self.userID = random.randrange(1001, 2002)
        self.regquerry = "insert into customers_reg (uname, pwd, fullname, phone_num) value(%s, %s, %s, %s)"
        self.regval = (self.username, self.password, self.fullname, self.phone)
        cursor.execute(self.regquerry, self.regval)
        conn.commit()
        print("Registration successful")
        self.operations()

    def login(self):
        self.user = input("enter your username: ")
        self.passs = input("enter your password: ")
        self.loginquerry = "select * from customers_reg where uname = %s and pwd = %s"
        self.loginval = (self.user, self.passs)
        cursor.execute(self.loginquerry, self.loginval)
        self.loginresult = cursor.fetchone()
        if self.loginresult is None:
            self.number_of_trials += 1
            print("invalid login")
            if self.number_of_trials >= 3:
                self.operations()
            else:
                self.login()
        else:
            print("login successful")
            self.status = "login"
            self.choice = input("Enter 1 to checkout\nEnter 2 to add to cart")
            if self.choice == "1":
                self.checkout()
            elif self.choice == "2":
                self.add_to_cart()
            else:
                self.operations()

    def checkout(self):
        if self.status == "not login":
            print("You are not yet logged in")
            self.login()
        else:
            print(f"this are the items in your cart\n{self.cart_category}\nthe price of the items in your cart is\n{self.price} ")
            self.pay = input("Enter 1 pay")
            if self.pay == "1":
                for category in self.cart_category:
                    for item in self.cart_items:
                        self.checkquery = "INSERT INTO sales_table (customer_id, product_name, product_price, quantity) values (%s, %s, %s, %s)"
                        self.checkval = (self.loginresult[0], item, self.price[item], self.cart_items[item])
                        cursor.execute(self.checkquery, self.checkval)
                        conn.commit()
                        self.itemquerry = f"update {category} set quantity = {'%s'} where product_name = {'%s'}"
                        self.newquantity = self.pickresult[3] - self.cart_items[item]
                        self.itemval = (self.newquantity, item)
                        cursor.execute(self.itemquerry, self.itemval)
                        conn.commit()
                        print(f"Checkout successful\nyou've successfully purchased {self.pick}")
            else:
                self.operations()
Ecommerce()


# products = {"food" : {"rice": 20, "beans": 50}, "drinks" : {"coke":20, "fanta":30}}
# for i in products:
#     cartitems = products[i]
#     for j in cartitems:
#         print(j)
#         print(cartitems[j])