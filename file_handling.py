# file = open("test1.txt","w")   #By default, it is in read mode
# file.write("Hello Biplav!")

file = open("test1.txt","r")
# print(file.read())
content = file.readlines()
for line in content:
    print(line)