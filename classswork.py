row = int(input("Enter the no of rows: "))
col = int(input("Enter the no of columns: "))

"""matrix = [
            [int(input()) for j in range(col)] 
                for i in range(row)
          ]"""
  
for i in range(row):
    for j in range(col):
        matrix=[[int(input())]*j]*i  
# print("The elements of matrix is:")
print(matrix)