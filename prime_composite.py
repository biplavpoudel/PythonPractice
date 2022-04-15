i = 2
n = input("Enter any number: ")
n = int(n)
while i <= n:
    if n%i == 0:
        break
    i = i+1
if n == i:
    print("prime")
else:
    print("composite")
    

