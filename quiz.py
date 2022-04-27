#A quiz program in Python

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

for i in range(len(question_list)):
    print("\n")
    print(question_list[i]['que'])
    print(question_list[i]['opt'])
    answer = input("Choose any option [a/b/c/d]:")
    
    if (answer == right_answer[i]):
        score += 1
        print("You are correct. +1 point")
    else:
        score -= 1
        print("You are wrong! -1 point")
        
print("\n\n")
if (score == 6):
    print("Perfect Score!")
elif (score >1 and score <6):
    print("You can do better!")
elif (score == 0):
    print("Booo!!!")
print("Your total score is: ", score)
print("\n")
