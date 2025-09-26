"""
Machines are good at crunching numbers - faster and more accurately than most 
humans! Create a small program that calculates something useful to you 
(making you smile is useful). It should take user input, at use at least one of the 
number operators we saw in class: + / * . You may modify one of your previous 
exercises to include calculations, if you wish.

Remember to design your algorithm in English first, then translate it to Python 
code. Test as you go!
"""
#Calculator Assignment
#Gabe Armour
#September 22, 2025

print("Hello, I am a calculator!")

print("Please enter your first number.")
firstNumber = float(input())

print("Please enter your operation (+, -, *, /).")
operation = str(input())

print("Please enter your second number.")
secondNumber = float(input())

if operation == "+":
    print(int(firstNumber + secondNumber))
    
if operation == "-":
    print(int(firstNumber - secondNumber))
    
if operation == "*":
    print(int(firstNumber * secondNumber))
    
if operation == "/":
    print(int(firstNumber / secondNumber))

