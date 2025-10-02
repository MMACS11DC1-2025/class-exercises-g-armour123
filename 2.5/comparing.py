"""
Create a program that uses counting and comparison operators (< > <= >=).
You must use the class' datafile, 'responses.csv' and analyze it
    to make at least 2 interesting observations.
You must use user input to add interactivity to the program.
You must design your algorithm in English first, then translate it to Python code.
Test as you go! Describe in your comments what steps you took to test your code.
"""
#Comparing assignment
#Gabe Armour
#Oct 2, 2025

#Algorithm:
#1. Open the file and read every row
#2. Ask for two names and find them in the file
#3. Compare their answers for each question
#4. Show most common food and pet as observations

file = open("2.4/responses.csv")
lines = file.readlines()

columns = ["Digit", "Pet", "Subject", "Play Sport", "Watch Sport", "Music", "Movie", "Food"]

rows = ""
for line in lines[1:]:
    parts = line.strip().split(",")
    if rows == "":
        rows = [parts]
    else:
        rows = rows + [parts]

print("Classmates:")
for r in rows:
    print(r[1])

firstName = input("Enter first name: ").strip()
secondName = input("Enter second name: ").strip()

firstRow = ""
secondRow = ""
for r in rows:
    if r[1].lower() == firstName.lower():
        firstRow = r
    if r[1].lower() == secondName.lower():
        secondRow = r

if firstRow == "" and secondRow == "":
    print("Both not found")
elif firstRow == "":
    print("First not found")
elif secondRow == "":
    print("Second not found")
else:
    same = 0

    columnNumber = 0
    for c in columns:
        a = firstRow[columnNumber + 2].strip()
        b = secondRow[columnNumber + 2].strip()
        print("\n" + c)
        print(firstRow[1] + ":", a)
        print(secondRow[1] + ":", b)

        if columnNumber == 0:
            x = int(a)
            y = int(b)
            print("==", x == y)
            print("<=", x <= y)
            if x == y:
                print("Result: Same digit")
                same = same + 1
            else:
                print("Result: Different digits")
        else:
            if a.lower() == b.lower():
                print("Result: Same")
                same = same + 1
            else:
                print("Result: Different")

        columnNumber = columnNumber + 1

    print("\nOverall, Same answers in", same, "out of", len(columns), "columns")

    foodList = ""
    foodNumber = ""
    for r in rows:
        food = r[9].strip()
        if food != "":
            if foodList == "":
                foodList = [food]
                foodNumber = [1]
            else:
                pos = 0
                found = False
                for f in foodList:
                    if f == food:
                        foodNumber[pos] = foodNumber[pos] + 1
                        found = True
                    pos = pos + 1
                if found == False:
                    foodList = foodList + [food]
                    foodNumber = foodNumber + [1]

    topFood = ""
    topfoodNumber = 0
    pos = 0
    for f in foodList:
        if foodNumber[pos] > topfoodNumber:
            topFood = f
            topfoodNumber = foodNumber[pos]
        pos = pos + 1

    petList = ""
    petNumber = ""
    for r in rows:
        pet = r[3].strip()
        if pet != "":
            if petList == "":
                petList = [pet]
                petNumber = [1]
            else:
                pos = 0
                found = False
                for p in petList:
                    if p == pet:
                        petNumber[pos] = petNumber[pos] + 1
                        found = True
                    pos = pos + 1
                if found == False:
                    petList = petList + [pet]
                    petNumber = petNumber + [1]

    topPet = ""
    toppetNumber = 0
    pos = 0
    for p in petList:
        if petNumber[pos] > toppetNumber:
            topPet = p
            toppetNumber = petNumber[pos]
        pos = pos + 1

    print("\nObservations")
    print("Most common fast food is", topFood)
    print("Most common pet is", topPet)

