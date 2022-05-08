# def addNumbers(num1,num2=0,num3=0):
#     # print(num2)
#     return num1+num2+num3
# sum = addNumbers(2)
def addNumbers(*num2):

   
   print(type(num2))
   sum =0
   for number in num2:
       sum += number
   return sum
#    return num1+num2
          
# print(addNumbers(2))
# print(addNumbers(2,3))
# print(addNumbers(2,3,4))


# print(addNumbers(num2=2,num1=1))
# num1 =2
# num2 =5

# sum = lambda num1,num2: num1+num2
# print(sum(2,5))

# nums = [i for i in range(1,21)]
# print(nums)


# evenNumbers = list(filter(lambda num: num % 2 == 0,nums))
# oddNumbers = list(filter(lambda num: num % 2 != 0,nums))
# # print(evenNumbers)
# # print(oddNumbers)


# Numbers = list(map(lambda num: num * 2 ,nums))
# print(Numbers)
# # filter first letter vowel

words = ['apple','ball','eye','dog']

vowels = list(filter(lambda word: word[0] in ['a','e', 'i','o','u'],words))
print(vowels)