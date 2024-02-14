def exam(self):
    import time
    nt = 0
    score = 0
    question = ["where is SQI located in Dugbe?", "SQI is which type of school?",
            "who is the president of Nigeria?", "which country won the last world cup?"]
    options = ["a. Heritage mall\nb. Central bank\nc. Cocoa House", 
                "a. coding school\nb. business school\nc. fashon school", 
                "a. perter obi\nb. tinubu\nc. atiku",
                "a. Agentina\nb. France\nc. Nigeria"]
    answer = ["a", "a", "c", "a"]
    for each in question:
        print(each)
        time.sleep(2)
        print(options[nt])
        ans = input("Enter your answer: ").strip().lower()
        an = answer[nt]
        if ans == an:
            print("you are correct")
            score += 10
        else:
            print("you are wrong")
            score -= 5
        nt += 1
        time.sleep(2)
    print(score)
exam()