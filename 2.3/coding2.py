"""
Write an Olympic Judging program that outputs the average scores from 5 different judges. 

Each score is out of 10 points maximum. Half points are allowed (e.g. 7.5)

The program should take 5 inputs and output the final average score.

Example:

Judge 1: 5.5
Judge 2: 10
Judge 3: 7
Judge 4: 8.5
Judge 5: 9
Your Olympic score is 8.0
"""

#Olympic Judging Program
#Gabe Armour
#Sep 23 2025

print("Hi there, please judge this performance out of 10, you are allowed to add decimals.")

print("Judge 1:")
judge1 = float(input())

print("Judge 2:")
judge2 = float(input())

print("Judge 3:")
judge3 = float(input())

print("Judge 4:")
judge4 = float(input())

print("Judge 5:")
judge5 = float(input())

finalScore = (judge1 + judge2 + judge3 + judge4 + judge5) / 5

print("Your olympic score is " + str(finalScore) + "!")