#A quiz program in Python
import time
import datetime

choice = input("Do you want to play the quiz: [yes/no] ")
while (choice == "yes"):
    name = input("Enter your name: ")
    # Getting starting time
    t1 = time.localtime()
    start_time = time.strftime("%H:%M:%S", t1)

    # Question Lists
    question_list = [
    {
        "que" : "1. What is the capital of Finland?",
        "opt" : {"a":"Helinski", "b":"Warsaw", "c":"Oslo", "d":"Stockholm"}
    },

    {
        "que" : "2. In Harry Potter, what is the name of The Weasley's house?",
        "opt" : {"a":"The Grimmauld Place", "b":"The Private Drive", "c":"The Burrow", "d":"The Godric's Hollow"}
    },

    {
        "que" : "3. What's a baby rabbit called?",
        "opt" : {"a":"A kit", "b":"A kid", "c":"A bunny", "d":"A ribbit"}
    },

    {
        "que" : "4. What is the strongest muscle in human body?",
        "opt" : {"a":"Tongue muscle", "b":"Jaw muscle", "c":"Hamstring", "d":"Abdominal muscle"}
    },

    {
        "que" : "5. What does the AC button on a calculator stand for?",
        "opt" : {"a":"Air Conditioner", "b":"ACcumulator", "c":"All Clear", "d":"Absolutely Continuous"}
    },

    {
        "que" : "6. How many bone does a shark have?",
        "opt" : {"a":"83", "b":"45", "c":"None", "d":"37"}
    }]

    right_answer = ["a","c","a","b","c","c"]

    score = 0
    # Asking the quiz to player
    for i in range(len(question_list)):
        print("\n")
        print(question_list[i]['que'])
        print(question_list[i]['opt'])
        answer = input("Choose any option [a/b/c/d]:")
    
        if (answer == right_answer[i]):
            score += 1
            print("You are correct. +1 point")
        else:
            score += 0
            print("You are wrong! 0 point")
    
    # Getting time at the end of quiz
    t2 = time.localtime()
    end_time = time.strftime("%H:%M:%S", t2)
    
    print("\n\n")
    if (score == 6):
        print("Perfect Score!")
    elif (score >1 and score <6):
        print("You can do better!")
    elif (score == 0):
        print("Booo!!!")
    print("Your total score is: ", score)
    print("\n")

    # Getting time taken to complete the quiz
    start_dt = datetime.datetime.strptime(start_time, '%H:%M:%S')
    end_dt = datetime.datetime.strptime(end_time, '%H:%M:%S')
    
    # Writing score to a file named "leaderboard.txt"
    file = open("C:\Python Practice\Quiz\leaderboard.txt","a")
    file.write(str(start_time) + "   " + str(end_time) + "   " + str(end_dt-start_dt) + "  " + name + "   " + str(score) + " \n")
    
    choice = input("Do you want to continue playing the quiz?: [yes/no] ")
    file.close()

    