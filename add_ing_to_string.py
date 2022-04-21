# Add -ing to the end of the string if string length is at least 3 char long. If -ing already exists, add -ly. Do nothing if string length is less than 3.
string = input("Enter any string: ")
length = len(string)
if length >=3 and string[-3:] != "ing":
    string1 = string + "ing"
    print("The new string is: ",string1)
elif length >=3 and string[-3:] == "ing":
    string2 = string + "ly"
    print("The new string is: ",string2)
else:
    quit