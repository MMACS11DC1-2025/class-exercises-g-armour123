"""
Make An Interactive Drawing or Animation 
Explore the turtle drawing package to create an interactive drawing.
It should use a while loop.
Your program should also include at least one function you've made yourself 
"""
import turtle
rylen = turtle.Turtle()
def draw_brownie(x, y):
	rylen.penup()
	rylen.goto(-100 + x, -100 + y)
	rylen.pendown()
	for i in range(2):
		length = 200
		width = 100
		rylen.forward(length)
		rylen.left(90)
		rylen.forward(width)
		rylen.left(90)
	rylen.penup()
	rylen.goto(-80 + x, -20 + y)
	rylen.stamp()
	rylen.goto(-48 + x, -43 + y)
	rylen.left(90)
	rylen.stamp()
	rylen.goto(-22 + x, -18 + y)
	rylen.stamp()
	rylen.goto(-3 + x, -61 + y)
	rylen.left(90)
	rylen.stamp()
	rylen.goto(-85 + x, -85 + y)
	rylen.stamp()
	rylen.goto(28 + x, -33 + y)
	rylen.stamp()
	rylen.goto(-35 + x, -82 + y)
	rylen.left(90)
	rylen.stamp()
	rylen.goto(70 + x, -15 + y)
	rylen.right(90)
	rylen.stamp()
	rylen.goto(30 + x, -80 + y)
	rylen.left(180)
	rylen.stamp()
	rylen.goto(56 + x, -56 + y)
	rylen.stamp()
	rylen.goto(75 + x, -82 + y)
	rylen.left(90)
	rylen.stamp()
	rylen.right(90)
while True:
	draw_brownie(0, 0)
	draw_brownie(100, 200)
	draw_brownie(-110, 200)
	break
turtle.done()
