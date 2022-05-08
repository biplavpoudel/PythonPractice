# Reading the leaderboard file
file = open("C:\Python Practice\Quiz/leaderboard.txt", "r")

name_list = []
new_list = []
maximum = 0
content = file.readlines()
for line in content:
    a = line.split()
    name_list.append(a)

# print(name_list[1][4])

for i in range(len(name_list)-1):
    maximum = name_list[i]
    # print(maximum)
    for j in range(1,len(name_list)):
        if(name_list[j][4] > maximum[4]):
            maximum = name_list[j]
            print(maximum)

# print(new_list)