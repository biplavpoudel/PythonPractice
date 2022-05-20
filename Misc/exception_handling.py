"""a,b = input("Enter any two numbers: ").split()
a = int(a)
b = int(b)
try:
    print(a/b)
except Exception:
    print("Exception caught")
else:
    print("Hello from else block")
finally:
    print("Inside finally")
    
print("Program Excecuted")"""

a = 10

class ChalkAndDusterException(Exception):   #Custom Exception Handling
    pass

try:
    if a % 2 == 0:
        raise ChalkAndDusterException()
    
except ChalkAndDusterException:
    print("ChalkAndDusterException caught")
except Exception:
    print("Exception caught")
else:
    print("Hello From else block")
finally:
    print("Inside finally")

print("Program executed")
    