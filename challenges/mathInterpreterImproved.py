#ask the user if they want to continue - if yes, continue, if no, end.
#incorrect operator format
#x or z are not numbers
#expression not in correct format. has more than 3 parts

def getInput():
    userInput = input("Expression: ")
    return userInput

def makeList(userInput):
    userList = userInput.split(" ")
    return userList

def getValue(list, index):
    value = list[index]
    return value

def performOperation(firstNumber, operation, secondNumber):
    if operation == "*":
        return (firstNumber * secondNumber)
    elif operation == "+":
        return (firstNumber + secondNumber)
    elif operation == "-":
        return (firstNumber - secondNumber)
    else:
        return (firstNumber / secondNumber)
    
def main():
    while True:
        length = 0

        while length != 3:
            userInput = getInput()
            userList = makeList(userInput)
            length = len(userInput)
            if length != 3:
                print("ERROR: please enter the expression in the correct format (x y z)")
        
        try:
            firstNumber = int(getValue(userList, 0))
        except:
            print("ERROR: didn't enter number for x.")
            break

        operation = getValue(userList, 1)
        if operation != "-" and operation != "+" and operation != "*" and operation != "/":
            print("ERROR: incorrect operator - only (+, -, *, /) allowed.")
            break
        
        try:
            secondNumber = int(getValue(userList, 2))
        except:
            print("ERROR: didn't enter number for z.")
            break
        answer = performOperation(firstNumber, operation, secondNumber)
        print(f"{answer:.1f}")

        while True:
            anotherCalculation = input("Would you like to evaluate another expression? (y/n) ").lower()
            if anotherCalculation == "y" or anotherCalculation == "n":
                break
        if anotherCalculation == "n":
            break

        #could also do if anotherCalculation != "y": break

main()