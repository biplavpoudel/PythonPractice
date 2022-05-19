# Randomized Quiz Game
import random

choice = input("Do you want to play the quiz: [yes/no] ")
while (choice == "yes"):
    # name = input("Enter your name: ")

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

    queList = [1,2,3,4,5,6]
    right_answer = ["a","c","a","b","c","c"]


    # Asking the quiz to player
    
    i = random.randrange(1,6)

    print(question_list[i]['que'])
    print(question_list[i]['opt'])
    answer = input("Choose any option [a/b/c/d]:")
    
    if (answer == right_answer[i]):
        print("You are correct.")
    else:
        print("You are wrong! ")

    choice = input("Do you want to continue playing the quiz?: [yes/no] ")


    