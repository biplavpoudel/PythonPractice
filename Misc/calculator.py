# Calculator App using Python

op = {
    1 : '+',
    2 : '-',
    3 : '*',
    4 : '/' 
}

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

answer = 'yes'

while( answer !='no' and answer == 'yes'):
    x,y = input("Enter two numbers: ").split()
    x = int(x)
    y = int(y)

    print("1:Addition\n 2:Subtraction\n 3:Multiplication\n 4.Division")
    operator = input("Enter your choice: ")

    print(x, op[int(operator)], y," = ", calc(operator))

    answer = input( "\nDo you want to continue? [yes/no] ")
    
