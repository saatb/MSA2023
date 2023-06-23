import random

#function that prompts for valid difficulty level and returns integer value of the difficulty - nothing passed into the function

#function that prompts for valid number of questions and returns integer value of the number of questions - nothing passed into the function

#function that generates both numbers in the equation - pass difficulty level into function

#use a variable to run a while loop 3 times

#CAN BE POLISHED

def getDifficultyLevel():
    difficultyLevel = ""
    validLevels = ["1", "2", "3"]
    while difficultyLevel not in validLevels:
        difficultyLevel = input("Enter difficulty level (1, 2, 3): \n")
        if difficultyLevel not in validLevels:
            print("ERROR: Invalid input! Please enter either 1, 2, or 3! \n")
    
    return int(difficultyLevel)


def getNumberOfQuestions():
    numberOfQuestions = ""
    validNumbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]
    while numberOfQuestions not in validNumbers:
        numberOfQuestions = input("Enter number of questions to ask (1-10): \n")
        if numberOfQuestions not in validNumbers:
            print("ERROR: Invalid input! Please enter a number between 1 and 10! \n")
    
    return int(numberOfQuestions)

def getEquation(diffLevel):
    if diffLevel == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif diffLevel == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    elif diffLevel == 3:
        x = random.randint(100, 999)
        y = random.randint(100, 999)

    return x, y

def main():
    difficultyLevel = getDifficultyLevel()
    numOfQuestions = getNumberOfQuestions()
    askedQuestions = 0
    correctQuestions = 0
    while askedQuestions != numOfQuestions:
        maxTries = 3
        userAnswer = ""
        num1, num2 = getEquation(difficultyLevel)
        answer = str(num1 + num2)
        while userAnswer != answer and maxTries != 0:
            userAnswer = input(f"{num1} + {num2} = ")
            if userAnswer != answer:
                print("WRONG!!!\n")
                maxTries -= 1
                if maxTries == 0:
                    print(f"Correct Answer: {num1} + {num2} = {answer} \n")
            else:
                print("CORRECT!!! \n")
                correctQuestions += 1
        askedQuestions += 1
    
    correctPercentage = (correctQuestions/numOfQuestions) * 100
    print(f"You got {correctQuestions} out of {numOfQuestions} correct: {correctPercentage:.2f}%")


main()