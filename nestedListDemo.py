#create a list
demoList = [15, 8, 64, 25, 9, 11, 32, 41]

listOfLists = [[2, 4, 7, 9],
               [3, 7, 8, 4], 
               [1, 8, 5, 2]]

print(demoList[2])

print(listOfLists[1][2])

print("\n")

#print all the values in listOfLists matrix
for list in listOfLists:
    for number in list:
        print(number)

#OR

for row in range(len(listOfLists)):
    print(f"\nRow {row + 1} Values")
    for column in range(len(listOfLists[row])):
        print(listOfLists[row][column])