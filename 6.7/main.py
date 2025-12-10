from PIL import Image
import time

def isRusty(r, g, b):
    return r > 120 and g > 80 and b < 80 

def isNotRusty(r, g, b):
    return r > 100 and g > 100 and b > 120 or r < 50 and g < 50 and b < 50

images = [
    "6.7/images/BlackRustSpots.jpg",
    "6.7/images/BrownishRust.jpg",
    "6.7/images/FullyRusted.jpg",
    "6.7/images/LineOfRust.jpg",
    "6.7/images/NoRust.jpg",
    "6.7/images/RustLines.jpg",
    "6.7/images/RustOnBlueMetal.avif",
    "6.7/images/RustOnSilver.jpg",
    "6.7/images/SlightlyRusted.jpg",
    "6.7/images/SpotsOfRust.jpg"
]
results = []

for files in images:
    file = Image.open(files)
    img = file.load()
    width = file.width
    height = file.height

    rustyPixels = 0
    notRustyPixels = 0
    t0 = time.time()
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
t1 = time.time()
totalTime = t1 - t0
print("Processed {} images in {:.3f} seconds".format(len(images), totalTime))


    
