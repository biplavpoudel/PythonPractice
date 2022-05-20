num = input("Enter any number: ")
num = int(num)
digit = num
sum = 0
while num > 0:
    k = num % 10
    sum = sum + k*k*k
    num =  int(num / 10)

if sum == digit:
    print("Armstrong")
else:
    print("Not Armstrong")
