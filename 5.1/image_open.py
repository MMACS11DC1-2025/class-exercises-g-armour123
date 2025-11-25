from PIL import Image
"""
image_green = Image.open("5.1/kid-green.jpg").load()
image_beach = Image.open("5.1/beach.jpg").load()
def isGreen(r, g, b):
    if r <= 100 and r >= 0 and g >= 150 and g <= 255 and b >= 0 and b <= 100:
        return True
    else:
        return False
# Create an output canvas C to draw on
image_output = Image.open("5.1/kid-green.jpg")

# Get width and height of the images
width = image_output.width
height = image_output.height

# Go through every pixel in A
for i in range(width):
    for j in range(height):
        r = image_green[i, j][0]
        g = image_green[i, j][1]
        b = image_green[i, j][2]

        # When the pixel is green, replace it with B's value
        if isGreen(r,g,b):
            beach_colour = image_beach[i, j] # Get beach colour at same spot
            image_output.putpixel((i, j), beach_colour) # Set the output pixel

# Save the resulting image in C
image_output.save("output.png", "png")
"""
#Question 1
"""
def is_light(pixel):
    r = pixel[0]
    g = pixel[1]
    b = pixel[2]
    avg = int((r + g + b) / 3)
    if avg >= 128:
        return True
    else: 
        return False

print(is_light((0, 0, 0)))
"""
#Question 2
from PIL import Image
image_beach = Image.open("5.1/beach.jpg").load()
output_image = Image.open("5.1/beach.jpg")
width = output_image.width
height = output_image.height


for i in range(width):
    for j in range(height):
        r = image_beach[i, j][0]
        g = image_beach[i, j][1]
        b = image_beach[i, j][2]
        
        if ((r + b + g) / 3) >= 128:
            xy = (i, j)
            colour1 = (255, 255, 255)
            output_image.putpixel(xy, colour1)
        else:
            colour2 = (0, 0, 0)
            output_image.putpixel(xy, colour2)
output_image.save("output.png")