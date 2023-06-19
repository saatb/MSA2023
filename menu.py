menu = {"Baja Taco": 4.00, "Burrito": 7.50, "Bowl": 8.50, "Nachos": 11.00, "Quesadilla": 8.50, "Super Burrito": 8.50, "Super Quesadilla": 9.50, "Taco": 3.00, "Tortilla Salad": 8.00 , "End": 0.00}

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

main()

