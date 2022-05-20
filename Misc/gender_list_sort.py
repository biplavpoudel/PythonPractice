male = ['Ram','Shyam','Hari','Ramesh','Sandip','Aashish','Rojesh','Biplav','Yogesh','Sharad']
female= ['Sita','Gita','Geeta','Radhika','Alisha','Katherine','Aayusha','Rakshya','Asha','Bimala']

name = input("Enter your name: ")
address = input("Enter your address: ")
DOB = int(input("Enter your date of birth: "))

if name in male:
    male1 = open("male1.txt","w")
    male1.write(name+ " is a male.")
    male1.write("\nHe lives in "+address)
    male1.write("\nHe is "+str(2022-DOB)+" years old.")
    male1.close()

elif name in female:
    female1 = open("female1.txt","w")
    female1.write(name+ " is a female.")
    female1.write("\nShe lives in "+address)
    female1.write("\nShe is "+str(2022-DOB)+" years old.")
    female1.close()