#Reading files in python
#open the file
dataFile = open("file.txt", "r")

#create an empty dictionary
menuItems = {}
#loop through data in the file
for lineOfData in dataFile:
    #what do we need to do to each line of data?
    #split lne of data at the ", "
    keysValues = lineOfData.split(", ")

    #create an entry to the dictionary, remember to convert price to float         
    menuItems[keysValues[0]] = float(keysValues[1])

dataFile.close()

for item, price in menuItems.items():
    print(f"{item}: ${price:.2f}")