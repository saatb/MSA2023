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
    userInput = getInput()
    userList = makeList(userInput)
    firstNumber = int(getValue(userList, 0))
    operation = getValue(userList, 1)
    secondNumber = int(getValue(userList, 2))
    answer = performOperation(firstNumber, operation, secondNumber)
    print(f"{answer:.1f}")

main()