# Convert two lists into a dictionary

from ast import Dict


keys = ['A','B','C']
values = [65,66,67]

dict={}

for i in range(0,len(keys)):
    dict[keys[i]] = values[i]

print(dict)