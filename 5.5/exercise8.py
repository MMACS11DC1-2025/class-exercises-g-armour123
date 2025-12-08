import time
t0 = time.time()
from PIL import Image
t1 = time.time()
file = Image.open("5.5/greem.jpg")
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

            if r > 180 and g > 100 and b < 100:
                yellow_pixels += 1
            if r < 100 and g < 50 and b > 150:
                blue_pixels += 1
            if r < 140 and g > 60 and b < 140:
                green_pixels += 1
            if r > 100 and g < 100 and b < 100:
                red_pixels += 1
            if r > 180 and g < 60 and b > 180:
                purple_pixels += 1
t3 = time.time()
percent_yellow = 100*yellow_pixels/(width*height)

percent_blue = 100*blue_pixels/(width*height)

percent_green = 100*green_pixels/(width*height)

percent_red = 100*red_pixels/(width*height)

percent_purple = 100*purple_pixels/(width*height)

# Calculate and output elapsed times
module_load = t1-t0
image_open_load = t2-t1
loop = t3-t2
entire = t3-t0
print(percent_green)
if percent_green >= 60:
    print("This image is very green")
else:
     print("This image is not very green")
timings = "It took {:.3f}s to import PIL, {:.3f}s to load the image, and {:.3f}s to do the loop. All in all it took {:.3f}s.".format(module_load, image_open_load, loop, entire)
print(timings)