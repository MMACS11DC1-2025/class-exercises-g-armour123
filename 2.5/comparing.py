"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""
#Comparing Assignment
#Gabe Armour
#Oct 8, 2025

#Algorithm
#1. Read the whole file
#2. Ask for two names in the file
#3. Compare all 8 answers (each row)
#4. Show 2 observations at the end

file = open("2.4/responses.csv")
lines = file.readlines()

rows = ""
for line in lines[1:]:
    line = line.strip()
    data = line.split(",")
    if rows == "":
        rows = [data]
    else:
        rows = rows + [data]

print("Classmates:")
for row in rows:
    print(row[1])

firstName = input("Enter first name: ").strip()
secondName = input("Enter second name: ").strip()

firstPerson = ""
secondPerson = ""

for row in rows:
    if row[1].lower() == firstName.lower():
        firstPerson = row
    if row[1].lower() == secondName.lower():
        secondPerson = row

if firstPerson == "" and secondPerson == "":
    print("Both not found")
elif firstPerson == "":
    print("First not found")
elif secondPerson == "":
    print("Second not found")
else:
    sameResults = 0

    #Favourite Digit
    firstDigit = int(firstPerson[2])
    secondDigit = int(secondPerson[2])
    print("Favourite Digit: " + str(firstDigit) + " vs " + str(secondDigit))
    if firstDigit == secondDigit:
        print("Result: Same digit")
        sameResults += 1
    else:
        print("Result: Different digits")

    #Favourite Pet
    print("Favourite Pet: " + firstPerson[3] + " vs " + secondPerson[3])
    if firstPerson[3].lower() == secondPerson[3].lower():
        print("Result: Same Favourite Pet")
        sameResults += 1
    else:
        print("Result: Different Favourite Pet")

    #Favourite School Subject
    print("Favourite Subject: " + firstPerson[4] + " vs " + secondPerson[4])
    if firstPerson[4].lower() == secondPerson[4].lower():
        print("Result: Same Favourite Subject")
        sameResults += 1
    else:
        print("Result: Different Favourite Subject")

    #Favourite Sport to Play
    print("Favourite Sport to Play: " + firstPerson[5] + " vs " + secondPerson[5])
    if firstPerson[5].lower() == secondPerson[5].lower():
        print("Result: Same Favourite Sport to Play")
        sameResults += 1
    else:
        print("Result: Different Favourite Sport to Play")

    #Favourite Sport to Watch
    print("Favourite Sport to Watch: " + firstPerson[6] + " vs " + secondPerson[6])
    if firstPerson[6].lower() == secondPerson[6].lower():
        print("Result: Same Favourite Sport to Watch")
        sameResults += 1
    else:
        print("Result: Different Favourite Sport to Watch")

    #Favourite Music Genre
    print("Favourite Music Genre: " + firstPerson[7] + " vs " + secondPerson[7])
    if firstPerson[7].lower() == secondPerson[7].lower():
        print("Result: Same Favourite Music Genre")
        sameResults += 1
    else:
        print("Result: Different Favourite Music Genre")

    #Favourite Movie Genre
    print("Favourite Movie Genre: " + firstPerson[8] + " vs " + secondPerson[8])
    if firstPerson[8].lower() == secondPerson[8].lower():
        print("Result: Same Favourite Movie Genre")
        sameResults += 1
    else:
        print("Result: Different Favourite Movie Genre")

    #Favourite Fast Food Restaurant
    print("Favourite Fast Food: " + firstPerson[9] + " vs " + secondPerson[9])
    if firstPerson[9].lower() == secondPerson[9].lower():
        print("Result: Same Favourite Fast Food")
        sameResults += 1
    else:
        print("Result: Different Favourite Fast Food")

    print("\nThey have " + str(sameResults) + " answers that are the same out of 8.")

    print("\nObservations:")
    if sameResults > 6:
        print(firstPerson[1] + " and " + secondPerson[1] + " have a lot in common!")
    elif sameResults == 5 or sameResults == 4:
        print(firstPerson[1] + " and " + secondPerson[1] + " have some things in common.")
    elif sameResults <= 3:
        print(firstPerson[1] + " and " + secondPerson[1] + " do not have a lot of things in common.")

    if firstDigit > secondDigit:
        print(firstPerson[1] + " picked a higher favorite digit than " + secondPerson[1] + ".")
    elif firstDigit < secondDigit:
        print(secondPerson[1] + " picked a higher favorite digit than " + firstPerson[1] + ".")
    else:
        print("They both picked the sam favorite digit.")

