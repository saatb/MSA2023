#list demo
names = ["John", "Mary", "Alice", "Bob"]
demoList = [10, 16, 24, 77, 2, 14, 9]

#add values to the list
demoList.append(5)
print(demoList, "\n")

#get number of items in a list
numberOfItems = len(demoList)
print(f"Number of items: {numberOfItems} \n")

#get values from the list
print(demoList[0])
print(demoList[4])

#print all items in list
print("\n")
for item in demoList:
    print(item)

#OR
print("/n")
for index in range(numberOfItems):
    print(demoList[index])

print("\n")
#print items at even indexes
for index in range(0, numberOfItems, 2):
    print(demoList[index])

print("\n")