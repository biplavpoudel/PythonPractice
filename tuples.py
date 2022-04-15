a = [1]
print(type(a))

a = tuple(a)
print(type(a))
print(a)

a = list(a)
a.append(7)
a = tuple(a)
print(type(a))
print(a)
