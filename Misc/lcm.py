def get_prime_factors(num):
    factors = []
    i = 2

    #Convert to odd
    while num % 2 == 0:
        factors.append(2)
        num //= 2

    for i in range(3, num, 2):
        if num % i == 0:
            factors.append(i)
            num //= i

    if num > 2:
        factors.append(num)

    print(factors)
    print(num) 
    return factors   
    
num1 = 64
num2 = 16

fact1 = get_prime_factors(num1)
fact2 = get_prime_factors(num2)

large = fact1
small = fact2

if len(fact1) < len(fact2):
    large = fact2
    small = fact1

lcm = []
for i in small:
    lcm.append(i)
    if i in large:
        large.remove(i)

lcm += large
print(lcm)
prod = 1
for i in lcm:
    prod *= i

print("LCM={}".format(prod))





