a = {
    2:"a",
    True:"True"
}

# print(a[True])
# print(a[1])

a["name"]= "Dipak"

# print(a)

a["name"] = "Biplav"   #update the value of key 'name'
# print(a)

for i, j in a.items():
    print(i,j)
 
ll = []   
for i,j in a.items():
    ll.append((i,j))    #Dictionary to List
print(ll)

lst = []
for i,j in a.items():   #Dictionary to Tuple
    lst.append((i,j))   
lst = tuple(lst)

print(lst)