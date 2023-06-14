#prompt the user to enter 2 numbers and output the sum of the two numbers

#Algorithm
#Inputs

#function to prompt user for an integer input
#function returns the integer

def getPositiveIntegerInput(num):
    while True:
        try:
            number = int(input(f"Enter the {num} value: "))
            if number <= 0:
                print("ERROR: Enter a value greater than 0. \n")
                #go back to the beginning of the loop
                continue
            break
        except ValueError:
            print("ERROR: please enter a valid number. \n")
    return number

def main():

    #1. ask the user for the first number and convert to an integer
    #if error occurs, reprompt the user to enter a correct value
    number1 = getPositiveIntegerInput("first")
    number2 = getPositiveIntegerInput("second")

    #Process data
    #3. Calculate the sum of the two numbers
    sumOfNumbers = number1 + number2

    #Output
    #4. print the answer to the user
    #"The answer to x + y = sum"
    print(f"The answer to {number1} + {number2} = {sumOfNumbers}")

main()