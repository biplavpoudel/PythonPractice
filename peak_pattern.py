# Create a peak(mountain) pattern in Python
#     *
#    ***
#   *****
#  *******
# *********

k = l = 5
m = 1
for i in range(1,6):
    string = ""
    for j in range(1,10):
       if j < k or l < j:
         string = string + " "  
       else:
           string = string + "*"
    print(string)
    k= k-1
    l = l+1
    m= m+2
        