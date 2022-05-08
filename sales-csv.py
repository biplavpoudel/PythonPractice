import csv

salesFile = open('sales-demo.csv')

salesDict = csv.DictReader(salesFile)
canceledOrders = []


# for line in salesFile.readlines():
#     print(line)

# for line in salesDict:
#     print(line)
#     if line['Status'].upper() == 'CANCELLED':
#         canceledOrders.append(line)

# print(canceledOrders)

# for items in canceledOrders:
#     print(items)

# total = 0.0
# for items in canceledOrders:
#     total += float(items['Total'])
# print(total)

name_filter = []
for line in salesDict:
    if line['Customer_Name'].upper() == 'MOHAMMED' or line['Customer_Name'].upper() == 'RAMESH':
    # if line['Customer_Name'].upper() in ['MOHAMMED','RAMESH']:
        name_filter.append(line)

# print(name_filter)

customFile = open("custom.csv",'w')   #'x' gives 'file aready exists error' else create new file like 'w'
# fields = ["Invoice_ID","Customer_Name","Product Name","Qty","Rate","Status","Total"]   
fields = ["Customer_Name","Status","Total"] 
writer = csv.DictWriter(customFile,fieldnames=fields)
writer.writeheader()

# writer.writerows(name_filter)
for line in name_filter:
    value = {
        'Customer_Name' : line['Customer_Name'],
        'Status' : line['Status'],
        'Total' : line['Total']
    }
    writer.writerow(value)

