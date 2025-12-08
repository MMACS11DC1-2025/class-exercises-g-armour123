from PIL import Image
import time

def isRusty(r, g, b):
    return r > 120 and g > 80 and b < 80 

def isNotRusty(r, g, b):
    return r > 100 and g > 100 and b > 120 or r < 50 and g < 50 and b < 50

images = [
    "6.7/BlackRustSpots.jpg",
    "6.7/BrownishRust.jpg",
    "6.7/FullyRusted.jpg",
    "6.7/LineOfRust.jpg",
    "6.7/NoRust.jpg",
    "6.7/RustLines.jpg",
    "6.7/RustOnBlueMetal.jpg",
    "6.7/RustOnSilver.jpg",
    "6.7/SlightlyRusted.jpg",
    "6.7/SpotsOFRust.jpg"
]
results = []
for files in images:
    file = Image.open(files)
    img = file.load()
    width = file.width
    height = file.height

    rustyPixels = 0
    notRustyPixels = 0

    for i in range(width):
        for j in range(height):
            r, g, b = img[i, j]
            if isRusty(r, g, b):
                rustyPixels += 1
            elif isNotRusty(r, g, b):
                notRustyPixels += 1

    totalPixels = rustyPixels + notRustyPixels
    rustinessPercent = rustyPixels / totalPixels * 100

    results.append((files, rustinessPercent))

    
