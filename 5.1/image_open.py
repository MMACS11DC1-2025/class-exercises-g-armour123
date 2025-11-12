from PIL import Image

image_green = Image.open("CS11/5.1/kid-green.jpg").load()
image_beach = Image.open("CS11/5.1/beach.jpg").load()
def isGreen(r, g, b):
    if r <= 25 and r >= 0 and g >= 230 and g <= 255 and b >= 0 and b <= 25:
        return True
    else:
        return False
print(image_green[0, 0])
pixel = image_green[0, 0]
r = pixel[0]
g = image_green[0, 0][1]
b = image_green[0, 0][2]

print(isGreen(r, g ,b))