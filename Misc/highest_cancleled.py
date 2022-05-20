import csv
salesFile = open('sales-demo.csv')

salesDict = csv.DictReader(salesFile)

canceledOrder = []

for line in salesDict:
    if line['Status'].upper() == 'CANCELLED':
        canceledOrder.append(line)

# print(canceledOrder)
# print(len(canceledOrder))

qty = 0
highestCanceled = {}
for line in canceledOrder:
    if line['Product Name'] in highestCanceled:
        qty = int(line['Qty']) + qty
    else:
        highestCanceled.update({line['Product Name'] : int(line['Qty'])})
# print(highestCanceled)

max = 0
name= []
for i,j in highestCanceled.items():
    if j>max:
        max=j
        name = i
print(name,max)
