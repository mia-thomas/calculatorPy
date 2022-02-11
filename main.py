#  Create a calculator function
# Write a Python function that accepts three parameters. 
# The first parameter is an integer. 
# The second is one of the following mathematical operators: +, -, /, or . The third parameter will also be an integer.

# The function should perform a calculation and return the results.
# For example, if the function is passed 6 and 4, it should return 24.

import math

def restart():
    print("Sorry, we did not catch that, please restart.")
    Game()

def anotherRound():
    anotherCalculation = input("Would you like to do another calculation today?")
    if anotherCalculation == "yes" or anotherCalculation == "Yes":
        print("Great, lets restart:")
        restart()
    elif anotherCalculation == "no" or anotherCalculation == "No":
        print("sorry to hear. goodbye! please come again!")
    else: print("I did not understand that, I will assume you said no. Goodbye!")

def Game():
    print("Calculator Game!")
    firstNumber = input("Please enter your first number:  ")
    mathOperator = input("Please select your Operator, would you like to subtract, multiply or add today?")
    secondNumber = input("We now need your second number:  ")
    if mathOperator == "subtract" or mathOperator == "Subtract" or mathOperator == "-":
        subtractStatement = int(firstNumber) - int(secondNumber)
        print(subtractStatement)
        anotherRound()
    elif mathOperator == "divide" or mathOperator == "Divide" or mathOperator == "/":
        divideStatement = int(firstNumber) / int(secondNumber)
        print(divideStatement)
        anotherRound()
    elif mathOperator == "add" or mathOperator == "Add" or mathOperator == "+":
        addStatement = int(firstNumber) + int(secondNumber)
        print(addStatement)
        anotherRound()
    else: restart()    

Game()

