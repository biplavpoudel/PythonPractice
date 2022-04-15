# Count the no of repetition of letters in any string
str = input("Enter any string: ")
str = str.lower()
# list = []

for i in range(0,len(str)):
    count = 0                     #counting no of times str[i] is repeated throughout the string
    # for c in str:
        # if str[i] not in list:
            # list.append(str[i])    #adding only non-repeated characters in list
    for j in range(0,len(str)):
        if str[i] == str[j]:
            count += 1
    print(str[i] ," is repeated ", count, " times")
# print(list)