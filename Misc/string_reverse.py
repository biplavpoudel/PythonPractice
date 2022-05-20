str = "Hello World"
# new_str = ""
# print(str[-1:0])
# print(len(str))
"""for i in range(len(str)-1,-1,-1):
    new_str = new_str + str[i]
print(new_str)"""

new_str = "".join(reversed(str))
print(new_str)

apple = "I love Apple"
print(apple.replace("A","Ma"))
print(apple.find('A'))