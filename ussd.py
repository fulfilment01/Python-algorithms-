"""create a ussd code compiler for the purchase of data
plan
"""
class ussd:
    def daily():
        opp = input("""1. N50 for 40MB\n2. N100 for 100MB\n3. N100 for 350MB(IG/TT/YT)\n4. N200 for 200MB\n5. N300 for 1GB\n6. N700 for 3GB\n7. N500 for 2GB\n8. N500 for 2.5GB: """)
        while opp not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            print("Invalid input. Enter 1-8")
            opp = input("""1. N50 for 40MB\n2. N100 for 100MB\n3. N100 for 350MB(IG/TT/YT)\n4. N200 for 200MB\n5. N300 for 1GB\n6. N700 for 3GB\n7. N500 for 2GB\n8. N500 for 2.5GB: """)
        else:
            if opp == '1':
                print("You selected option 1: N50 for 40MB")
                opp1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back: """)
                while opp1 not in ["1", "2", "3", "4"]:
                    print("Unknown Application")
                    opp1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back: """)
                else:
                    print("successful")
            elif opp == '2':
                print("You selected option 2: N100 for 100MB")
                opp1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back: """)
                while opp1 not in ["1", "2", "3", "4"]:
                    print("Unknown Application")
                    opp1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back: """)
                else:
                    print("successful")
            elif opp == '3':
                print("You selected option 3: N100 for 350MB(IG/TT/YT)")
                opp1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back: """)
                while opp1 not in ["1", "2", "3", "4"]:
                    print("Unknown Application")
                    opp1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back: """)
                else:
                    print("successful")
            elif opp == '4':
                print("You selected option 4: N200 for 200MB")
                opp1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back: """)
                while opp1 not in ["1", "2", "3", "4"]:
                    print("Unknown Application")
                    opp1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back: """)
                else:
                    print("successful")
            elif opp == '5':
                print("You selected option 5: N300 for 1GB")
                opp1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back: """)
                while opp1 not in ["1", "2", "3", "4"]:
                    print("Unknown Application")
                    opp1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back: """)
                else:
                    print("successful")
            elif opp == '6':
                print("You selected option 6: N700 for 3GB")
                opp1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back: """)
                while opp1 not in ["1", "2", "3", "4"]:
                    print("Unknown Application")
                    opp1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back: """)
                else:
                    print("successful")
            elif opp == '7':
                print("You selected option 7: N500 for 2GB")
                opp1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back: """)
                while opp1 not in ["1", "2", "3", "4"]:
                    print("Unknown Application")
                    opp1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back: """)
                else:
                    print("successful")
            elif opp == '8':
                print("You selected option 8: N500 for 2.5GB")
                opp1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back: """)
                while opp1 not in ["1", "2", "3", "4"]:
                    print("Unknown Application")
                    opp1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back: """)
                else:
                    print("successful")


    def weekly():
        opps = input("""1. N300 for 350MB\n2. N200 for 1GB(IG/TT/YT)\n3. N500 for 1.5GB\n4. N500 for 750MB+N500(14days)\n5. N500 for 1GB\n6. N1,800 for 7GB\n7. N1,000 for 2GB\n: """)
        while opps not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Enter your choice (1-7): ")
            opps = input("""1. N300 for 350MB\n2. N200 for 1GB(IG/TT/YT)\n3. N500 for 1.5GB\n4. N500 for 750MB+N500(14days)\n5. N500 for 1GB\n6. N1,800 for 7GB\n7. N1,000 for 2GB\n: """)
        else:
            if opps == '1':
                print("you will be charged N300 for\n 350MB+350MB YouTube Night\n Weekly plan ")
                opps1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                while opps1 not in ["1", "2", "3", "4"]:
                    print("Unknown Application")
                    opps1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                else:
                    print("successful")
            elif opps == '2':
                print("you will be charged N200 for\n 1GB Instagram/TiTok/YouTube weekly\n bundle valid for 7Days")
                opps1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                while opps1 not in ["1", "2", "3", "4"]:
                    print("Unknown Application")
                    opps1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                else:
                    print("successful")
            elif opps == '3':
                print("you will be charged N500 for the\n purchase of 750MB+1.5GBYouTube\n Bi-weekly plan.")
                opps1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                while opps1 not in ["1", "2", "3", "4"]:
                    print("Unknown Application")
                    opps1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                else:
                    print("successful")
            elif opps == '4':
                print("Buy XtraData500 @N500 and get\n N500 talktime+750MB valid for\n 14days.")
                opps1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                while opps1 not in ["1", "2", "3", "4"]:
                    print("Unknown Application")
                    opps1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                else:
                    print("successful")
            elif opps == '5':
                print("you will be charged N500 for\n 1GB+1GB YouTube Night\n Weekly plan ")
                opps1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                while opps1 not in ["1", "2", "3", "4"]:
                    print("Unknown Application")
                    opps1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                else:
                    print("successful")
            elif opps == '6':
                print("you will be charged N1,800 for\n 7GB Weekly plan ")
                opps1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                while opps1 not in ["1", "2", "3", "4"]:
                    print("Unknown Application")
                    opps1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                else:
                    print("successful")
            elif opps == '7':
                print("you will be charged N1000 for the\n purchase of 2GB Weekly plan.")
                opps1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                while opps1 not in ["1", "2", "3", "4"]:
                    print("Unknown Application")
                    opps1 = input("""To proceed, select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                else:
                    print("successful")

    def monthly():
        oppe = input("""1. N1,000 for 1.5GB\n2. N1200 for 2GB\n3. N1,500 for 3GB\n4. N2000 for 4.5GB\n5. N2,500 for 6GB\n6. N3,500 for 12GB\n7. N5,000 for 20GB\n8. N6000 for 25GB\n: """)
        while oppe not in ["1", "2", "3", "4", "5", "6", "7"]:
            print("Enter your choice(1-7)")
            oppe = input("""1. N1,000 for 1.5GB\n2. N1200 for 2GB\n3. N1,500 for 3GB\n4. N2000 for 4.5GB\n5. N2,500 for 6GB\n6. N3,500 for 12GB\n7. N5,000 for 20GB\n8. N6000 for 25GB\n: """)
        else:
            if oppe == "1":
                print("You will be charged N1,000 for the\n purchase of 1.5GB Monthly Plan.")
                oppe1 = input("""To proceed,select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                while oppe1 not in ["1", "2", "3", "4"]:
                    print("Unknown Application")
                    oppe1 = input("""To proceed,select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                else:
                    print("successful")
            elif oppe == "2":
                print("You will be charged N1,200 for the\n purchase of 2GB Monthly Plan.")
                oppe1 = input("""To proceed,select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                while oppe1 not in ["1", "2", "3", "4"]:
                    print("Unknown Application")
                    oppe1 = input("""To proceed,select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                else:
                    print("successful")
            elif oppe == "3":
                print("You will be charged N1,500 for the\n purchase of 3GB Monthly Plan.")
                oppe1 = input("""To proceed,select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                while oppe1 not in ["1", "2", "3", "4"]:
                    print("Unknown Application")
                    oppe1 = input("""To proceed,select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                else:
                    print("successful")
            elif oppe == "4":
                print("You will be charged N2,000 for the\n purchase of 4.5GB Monthly Plan.")
                oppe1 = input("""To proceed,select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                while oppe1 not in ["1", "2", "3", "4"]:
                    print("Unknown Application")
                    oppe1 = input("""To proceed,select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                else:
                    print("successful")
            elif oppe == "5":
                print("You will be charged N2,500 for the\n purchase of 6GB Monthly Plan.")
                oppe1 = input("""To proceed,select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                while oppe1 not in ["1", "2", "3", "4"]:
                    print("Unknown Application")
                    oppe1 = input("""To proceed,select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                else:
                    print("successful")
            elif oppe == "6":
                print("You will be charged N3,500 for the\n purchase of 12GB Monthly Plan.")
                oppe1 = input("""To proceed,select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                while oppe1 not in ["1", "2", "3", "4"]:
                    print("Unknown Application")
                    oppe1 = input("""To proceed,select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                else:
                    print("successful")
            elif oppe == "7":
                print("You will be charged N5,000 for the\n purchase of 20GB Monthly Plan.")
                oppe1 = input("""To proceed,select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                while oppe1 not in ["1", "2", "3", "4"]:
                    print("Unknown Application")
                    oppe1 = input("""To proceed,select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                else:
                    print("successful")
            elif oppe == "8":
                print("You will be charged N6,000 for the\n purchase of 25GB Monthly Plan.")
                oppe1 = input("""To proceed,select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                while oppe1 not in ["1", "2", "3", "4"]:
                    print("Unknown Application")
                    oppe1 = input("""To proceed,select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                else:
                    print("successful")

    def months2_3():
        opper = input("""1. N8000 for 30GB\60Days\n2. N20,000 for 100GB\60Days\n3. N30,000 for 160GB\60Days\n4. N50,000 for 400GB\90Days\n5. N75,000 for 600GB\90Days\n0. Back: """)
        while opper not in ["1", "2", "3", "4", "5"]:
            print("Enter a choice (1_7)")
            opper = input("""1. N8000 for 30GB\60Days\n2. N20,000 for 100GB\60Days\n3. N30,000 for 160GB\60Days\n4. N50,000 for 400GB\90Days\n5. N75,000 for 600GB\90Days\n0. Back: """)
        else:
            if opper == "1":
                print("You will be chaarged N8000 for the\n purchase of 30GB 2-Month Plan.")
                opper1 = input("""To proceed, seleect:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                while opper1 not in ["1", "2", "3", "4"]:
                    opper1 = input("""To proceed,select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                else:
                    print("successful")
            elif opper == "2":
                print("You will be chaarged N20,000 for the\n purchase of 100GB 2-Month Plan.")
                opper1 = input("""To proceed, seleect:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                while opper1 not in ["1", "2", "3", "4"]:
                    opper1 = input("""To proceed,select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                else:
                    print("successful")
            elif opper == "3":
                print("You will be chaarged N30,000 for the\n purchase of 160GB 2-Month Plan.")
                opper1 = input("""To proceed, seleect:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                while opper1 not in ["1", "2", "3", "4"]:
                    opper1 = input("""To proceed,select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                else:
                    print("successful")
            elif opper == "4":
                print("You will be chaarged N50,000 for the\n purchase of 400GB 3-Month Plan.")
                opper1 = input("""To proceed, seleect:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                while opper1 not in ["1", "2", "3", "4"]:
                    opper1 = input("""To proceed,select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                else:
                    print("successful")
            elif opper == "5":
                print("You will be chaarged N75,000 for the\n purchase of 600GB 3-Month Plan.")
                opper1 = input("""To proceed, seleect:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                while opper1 not in ["1", "2", "3", "4"]:
                    opper1 = input("""To proceed,select:\n1. Auto-Renew\n2. One-off\n3. Buy for a Friend\n4. Redeem Promo Code\n0. Back\n: """)
                else:
                    print("successful")
            else:
                print("Unknown Application")
            
    code = input("dial *312#: ")
    if code == "*312#":
        operation = input("""Enter 1. Data Plans\n: """)
        if operation == '1': 
            print("Buy Data Plans")
            operations = input("""Enter 1. Daily\nEnter 2. Weekly\nEnter 3. Monthly\nEnter 4. 2-3Month\nEnter 5. Always ON\n: """)
            if operations == '1':
                print("For daily bundles")
                daily()

            elif operations == "2":
                print("for weekly bundles")
                weekly()
                
            elif operations == "3":
                print("montly plan")
                monthly()

            elif operations == "4":
                print("2-3Month Plans")
                months2_3()
                
            elif operations == "5":
                print("Always On Bundle")
                oper = input("""1. N60 for 20MB/24 Hrs\n2. N120 for 450MB/30 Days\n3. N3000 for 15GB/30 Days\n4. N6000 for 45GB/30 Days\n0. Back\n00. MainMenu: """)
            else :
                print(operation)
        else:
            print(operation)
    else:
     print("code error")
ussd()