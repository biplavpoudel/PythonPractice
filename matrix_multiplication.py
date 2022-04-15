row1 = int(input("Enter no of rows of matrix A: "))
col1 = int(input("Enter no of columns of matrix A: "))
row2 = int(input("Enter no of rows of matrix B: "))
col2 = int(input("Enter no of columns of matrix B: "))

if col1 != row2:
    print("\nMatrix Multiplication is not possible!\n")
    exit()
    
#Creating matrices A and B
print("Enter the elements of matrix A: ")
matrix1 = [[int(input()) for j in range(col1)] for i in range(row1)]
print("\nEnter elements of matrix B: ")
matrix2 = [[int(input()) for j in range(col2)] for i in range(row1)]

#Printing the original contents of A and B
print("\nThe matrix A is:")
for items in matrix1:
    print(items)
    
print("\nThe matrix B is:")
for items in matrix2:
    print(items)
    
#Creating an empty matrix of size: row1*col2
matrix3 = [[0 for j in range(col2)] for i in range(row1)]
sum = 0
#Now for multiplication
for i in range(row1):
    for j in range(col2):
        for k in range(row2):
            sum = sum + matrix1[i][k]*matrix2[k][j]
        matrix3[i][j] = sum
        sum = 0
        
#For final resulatant matrix
print("\nThe product of matrices A and B is: ")
for items in matrix3:
    print(items)