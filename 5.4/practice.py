#Gabe Armour
#Nov 19, 2025
#White jellybean conversion assignment
# Import image processing libraries
# Define a function colour(r,g,b) to return the colour of a pixel
"""
def colour(r, g, b):
# Yellow
    if r > 150 and g > 150 and b < 150:
        return "yellow"
        # Other
    else:
        return "other"

# Load an image of jellybeans
file = Image.open("5.4/jelly_beans.jpg")
jb_image = file.load()
output_image = Image.open("5.4/jelly_beans.jpg")
# Create a list to store the pixels that are yellow
yellow_pixels = []

# Go through all the pixels in the image
width = file.width
height = file.height
for x in range(width):
    for y in range(height):
        pixel_r = jb_image[x,y] [0]
        pixel_g = jb_image[x,y][1]
        pixel_b = jb_image[x,y][2]
        
        if colour(pixel_r, pixel_g, pixel_b) == "yellow":
            white = (255, 255, 255)
            output_image.putpixel((x, y), white)
output_image.save("output.png")
"""
#Takes an image as input and outputs the percentage of each jellybean colour in the image
# First, let's try calculating the percentage of yellow jellybeans and outputting that.
# Load the image

import time
t0 = time.time()
from PIL import Image
t1 = time.time()
file = Image.open("5.4/jelly_beans.jpg")
jbimg = file.load()

# Go through all the pixels in the image
width = file.width
height = file.height

# Initialize a counter
yellow_pixels = 0
blue_pixels = 0
green_pixels = 0
red_pixels = 0
purple_pixels = 0
t2 = time.time()
for i in range(width):
    for j in range(height):
    # If the pixel is yellow ~(255,255,0), add it to a list or counter
            r = jbimg [i, j] [0]
            g = jbimg [i, j] [1]
            b = jbimg[i, j] [2]

            if r > 100 and g > 100 and b < 100:
                yellow_pixels += 1
            if r < 100 and g < 100 and b > 100:
                blue_pixels += 1
            if r < 100 and g > 70 and b < 100:
                green_pixels += 1
            if r > 100 and g < 100 and b < 100:
                red_pixels += 1
            if r > 100 and g < 100 and b > 100:
                purple_pixels += 1
t3 = time.time()
percent_yellow = 100*yellow_pixels/(width*height)
yellow_report = "There are {:.2f} percent yellow jellybeans.".format(percent_yellow)
print(yellow_report)

percent_blue = 100*blue_pixels/(width*height)
blue_report = "There are {:.2f} percent blue jellybeans.".format(percent_blue)
print(blue_report)

percent_green = 100*green_pixels/(width*height)
green_report = "There are {:.2f} percent green jellybeans.".format(percent_green)
print(green_report)

percent_red = 100*red_pixels/(width*height)
red_report = "There are {:.2f} percent red jellybeans.".format(percent_red)
print(red_report)

percent_purple = 100*purple_pixels/(width*height)
purple_report = "There are {:.2f} percent purple jellybeans.".format(percent_purple)
print(purple_report)

# Calculate and output elapsed times
module_load = t1-t0
image_open_load = t2-t1
loop = t3-t2
entire = t3-t0

timings = "It took {:.2f}s to import PIL, {:.2f}s to load the image, and {:.2f}s to do the loop. All in all it took {:.2f}s.".format(module_load, image_open_load, loop, entire)
print(timings)