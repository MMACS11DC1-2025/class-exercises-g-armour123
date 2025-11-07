import turtle

def drawSnowflake(level, length):
    #Base case (stop recursion)
    if level == 0:
        turtle.forward(length)
        return 1  #Count this call

    #Count for this call
    count = 1

    #Make smaller lines each time
    length = length / 3

    #Draw 4 smaller parts (Koch curve pattern)
    count += drawSnowflake(level - 1, length)
    turtle.left(60)
    count += drawSnowflake(level - 1, length)
    turtle.right(120)
    count += drawSnowflake(level - 1, length)
    turtle.left(60)
    count += drawSnowflake(level - 1, length)

    return count


def main():
    print("Welcome to the Recursive Snowflake Generator!")
    print("This program draws a snowflake using recursion.\n")
    
    

    #Input for recursion depth
    level = -1
    while True:
        userInput = input("Enter recursion depth (0-5): ")
        if userInput.isdigit():
            level = int(userInput)
            if level >= 0 and level <= 5:
                break
            else:
                print("Please enter a number between 0 and 5.")
        else:
            print("That's not a number! Try again.")

    #Input for snowflake size
    length = 0
    while True:
        userInput = input("Enter snowflake size (50-350): ")
        if userInput.isdigit():
            length = int(userInput)
            if length <= 350 and length >= 50:
                break
            else:
                print("Please enter a number between 50 and 400.")
        else:
            print("That's not a number! Try again.")

    #Dictionary for basic settings
    settings = {
        "depth": level,
        "color": "lightblue",
        "speed": "fastest",
        "background": "navy"
    }

    #Setup turtle
    screen = turtle.Screen()
    screen.bgcolor(settings["background"])
    turtle.color(settings["color"])
    turtle.speed(settings["speed"])
    turtle.penup()
    turtle.goto(-length / 2, length / 3)
    turtle.pendown()

    #Draw 3 sides for the full snowflake
    totalCalls = 0
    for i in range(3):
        totalCalls += drawSnowflake(level, length)
        turtle.right(120)

    #Print total recursive calls
    print("\nTotal recursive calls made:", totalCalls)
    turtle.done()


#Run the program
main()
