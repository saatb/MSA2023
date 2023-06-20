def getMenuDictionary():
    menuFile = open("file.txt", "r")
    menu = {}
    for lineOfData in menuFile:
        keyValues = lineOfData.split(", ")
        menu[keyValues[0]] = float(keyValues[1])
    
    menuFile.close()
    return menu
    


def getValidInput():
    userInput = ""
    while userInput not in menu:
        userInput = input("Item: ")
        userInput = userInput.title()

    return userInput

def getItemValue(item):
    value = menu[item]
    return value

def main():
    total = 0
    while True:
        menuInput = getValidInput()

        if menuInput == "End":
            break
        
        itemValue = getItemValue(menuInput)
        total += itemValue
        print(f"Total: ${total:.2f}")
        print("\n")

menu = getMenuDictionary()

main()