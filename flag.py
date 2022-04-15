i = 1
count = 1
while i <= 10:
    if (i %5 == 0):
        print ("*" * 5)
    else:
        print("*" * count)
    count = (count+1) % 5
    i += 1
