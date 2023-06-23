def getValidInput(amountDue): #pass amountDue in so that i can print it alongside the user prompt to enter a coin
    userInput = ""
    while userInput != "1" and userInput != "5" and userInput != "10" and userInput != "25": #checks to make sure that input is a valid denomination of coin - don't convert here so that i don't have to deal with value errors!
        print(f"Amount Due: {amountDue}")
        userInput = input("Insert Coin: \n")

    return userInput

def checkChange(amountDue):
    amountDue = 0 - amountDue #absolute value of the amount due

    print(f"Change Owed: {amountDue}")

def main():
    amountDue = 50 #set up initial cost of the item - 50 cents
    while amountDue > 0:
        userInput = int(getValidInput(amountDue)) #convert to int here because i know that it will be a valid string
        amountDue -= userInput #change amount due based on how much the user inputs
    
    checkChange(amountDue)
        

main()