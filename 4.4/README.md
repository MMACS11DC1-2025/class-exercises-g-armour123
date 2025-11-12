# Recursive Fractal Art Generator – Snowflake Edition  
**By:** Gabe Armour 
**Course:** CS11  
**Project:** Mini-Project – Recursive Fractal Art Generator  



## Project Overview
This program draws a Koch Snowflake Fractal using recursion and turtle graphics in Python.  
It asks the user for the recursion depth and the snowflake size, then uses the function to draw a snowflake pattern made of smaller repeating triangles.
The purpose of this project is to show how recursion can be used to create detailed patterns by repeating the same drawing steps at smaller scales.



## How It Works
1. The user enters the recursion depth (0-5) and the snowflake size (50-350).  
2. The code checks if the inputs that the user made are valid, and if they aren't, it asks again.  
3. The drawSnowflake(level, length) function draws one side of the snowflake, calls itself four times each time it runs, making smaller pieces, and stops when the base case is reached.  
4. The turtle turns three times, 120° each to draw all of the sides.  
5. At the end, the program prints the total number of recursive calls.  


## Recursive Approach Explained
- **Recursive Function:** drawSnowflake(level, length) 
- **Base Case:** When level == 0, the function draws a straight line.  
- **Recursive Step:** When the level > 0, the function divides the line into 3 smaller parts and draws four smaller snowflake sections. Each call gets smaller until it reaches the base case.


## Why It Works
Each recursive call adds more detail to the snowflake.  
At depth 0, it’s just a triangle.  
At depth 3 or 4, it becomes a detailed snowflake made of smaller triangles.  
Because of the base case, the recursion eventually stops and doesn’t loop forever.


## How To Run It
1. Open any Python IDE.  
2. Save the program as main.py.  
3. Run the file.  
4. Type the recursion depth and snowflake size.
5. Boom!  

## Peer Review
- My Peer Reviewer was Mason
- He said everything was good
- Suggested to add a background color or to add multiple snowflakes
- I added a background color, not sure how to add multiple snowflakes, and multiple snowflakes would overlap if the user made too big of a size
## Test Cases

### Test Case 1: Base Case (Depth = 0)
### Input: 
- **Recursion Depth:** 0
- **Snowflake Size:** 50
### Expected Output:
- **A Small Triangle**
### Real Output:
![alt text](<Screenshot 2025-11-10 124556.png>)
- **Testing Successful**