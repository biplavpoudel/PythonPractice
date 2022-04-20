# Filtering words in a text by replacing

# from dataclasses import replace


file = open("input_word_filter.txt","r")
file2 = open("output_word_filter.txt","w")
lst=[]
str = " "
for word in file.read().split():   #split() is used to separate words as per space
    lst.append(word)
    
    
for items in lst:
    file2.write(str)
    items = items.replace("God","G*d")
    items = items.replace("GOD","G*D")
    items = items.replace("god","g*d")
    file2.write(items)

file.close()
file2.close()