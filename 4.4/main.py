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

    #Simple user inputs
    level = int(input("Enter recursion depth (0-5): "))
    length = int(input("Enter the snowflake size: "))

    #Dictionary for basic settings
    settings = {
        "depth": level,
        "color": "lightblue",
        "speed": "fastest"
    }

    #Setup turtle
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
