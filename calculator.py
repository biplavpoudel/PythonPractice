# Calculator App in Python
x,y = input("Enter two numbers: ").split()
x = int(x)
y = int(y)


print("1:Addition\n 2:Subtraction\n 3:Multiplication\n 4.Division")
operator = input("Enter your choice: ")


def calc(operator):
    match operator:
        case '1':
            return x+y
        case '2':
            return x-y
        case '3':
            return x*y
        case '4':
            return x/y

print("The arithmetic operation of",x," and ",y," is ", calc(operator))