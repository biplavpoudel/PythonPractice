name = input("Please kindly state your name: ")
address = input("Your Address? ")
DOB = int(input("Your DOB in AD: "))
gender = input("Enter your gender: ")
gender = gender.lower()
year = 2022


if gender == "male" or gender == 'm':
    male = open("male.txt","w")
    male.write(name + " is a ")
    male.close()
    
    male = open("male.txt","a")
    male.write(gender+ " of age "+str(year-DOB)+" born in " +str(DOB)+ " living in "+ address+ ".")
    male.close()
    
elif gender == "female" or gender =='f':
    female = open("female.txt","w")
    female.write(name + " is a ")
    female.close()
    
    female = open("female.txt","a")
    female.write(gender+ " of age "+str(year-DOB)+" born in " +str(DOB)+ " living in "+ address+ ".")
    female.close()
else:
    print("Please select either of the two for the time being. No sexual prejudice intended.")