row = int(input("Enter the no of rows: "))
column = int(input("Enter the no of columns: "))

print("Enter the elements of matrix: ")
matrix = [[int(input()) for j in range(column)] for i in range(row)]

print("\n")
print("The original matrix is: ")
for items in matrix:
    print(items)

# Now we create a schema for transposed matrix and fill it with zero
solution = [[0 for i in range(row)] for j in range(column)]  #Notice the interchange of rows and columns in list comprehension

# Now the actual transposition occurs here

for i in range(row):
    for j in range(column):
        solution[j][i] = matrix[i][j]

print("\n")
print("The transposed matrix is: ")
for items in solution:
    print(items)

