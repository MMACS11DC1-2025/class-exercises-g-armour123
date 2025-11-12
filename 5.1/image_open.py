from PIL import Image

image_green = Image.open("CS11/5.1/kid-green.jpg").load()
image_beach = Image.open("CS11/5.1/beach.jpg").load()
def isYellow(r, g, b):
    if r <= 255 and r >= 230 and g >= 230 and g <= 255 and b >= 0 and b <= 25:
        return "Yellow"
    else:
        return "Not yellow"
print(image_green[0, 0])
pixel = image_green[0, 0]
r = pixel[0]
g = image_green[0, 0][1]
b = image_green[0, 0][2]

print(isYellow(r, g ,b))