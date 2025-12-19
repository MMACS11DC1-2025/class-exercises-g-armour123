#Algorithm (In Simple English):
#1. Load a list of images showing metal surfaces.
#2. For each image, check every pixel using nested loops.
#3. Count how many pixels look rusty and how many do not.
#4. Calculate the rust percentage for each image.
#5. Convert the rust percentage into a rust level from 1 to 4.
#6. Store the image name, rust percentage, and rust level in a list.
#7. Sort the list from highest rust level to lowest using Selection Sort.
#8. Display the top 5 most rusted images.
#9. Use Binary Search to check if a specific rust level exists.
#10. Print all images that match the searched rust level.

from PIL import Image
import time

#Function to detect rust pixels
def isRusty(r, g, b):
    return r > 120 and g > 80 and b < 80

#Function to detect non-rust pixels (clean metal or background)
def isNotRusty(r, g, b):
    return (r > 100 and g > 100 and b > 120) or (r < 50 and g < 50 and b < 50)

#Convert rust percentage into a rust level (1-4). This is easier as we don't need exact percentages later.
def getRustLevel(rustPercent):
    if rustPercent < 10:
        return 1
    elif rustPercent < 30:
        return 2
    elif rustPercent < 60:
        return 3
    else:
        return 4

#Selection Sort function (highest rust level to lowest)
def selectionSort(data):
    for i in range(len(data)):
        maxIndex = i
        for j in range(i + 1, len(data)):
            if data[j][2] > data[maxIndex][2]:
                maxIndex = j
        data[i], data[maxIndex] = data[maxIndex], data[i]

#Binary Search for a specific rust level
def binarySearch(data, targetLevel):
    startIndex = 0
    endIndex = len(data) - 1

    while startIndex <= endIndex:
        mid = (startIndex + endIndex) // 2
        midLevel = data[mid][2]

        if midLevel == targetLevel:
            return True
        elif midLevel < targetLevel:
            endIndex = mid - 1
        else:
            startIndex = mid + 1

    return False

#List of images to analyze
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

#Start timing
t0 = time.time()

#Process each image
for files in images:
    image = Image.open(files)
    pixels = image.load()
    width = image.width
    height = image.height

    rustyPixels = 0
    notRustyPixels = 0

    for x in range(width):
        for y in range(height):
            r, g, b = pixels[x, y]
            if isRusty(r, g, b):
                rustyPixels += 1
            elif isNotRusty(r, g, b):
                notRustyPixels += 1

    totalPixels = rustyPixels + notRustyPixels

    if totalPixels > 0:
        rustinessPercent = (rustyPixels / totalPixels) * 100
    else:
        rustinessPercent = 0

    rustLevel = getRustLevel(rustinessPercent)

    #Store filename, percentage, and rust level
    results.append((files, str(rustinessPercent) + "%", rustLevel))

#End timing
t1 = time.time()
totalTime = t1 - t0

print("Processed {} images in {:.3f} seconds".format(len(images), totalTime))

#Sort results by rust level
selectionSort(results)

print("\nImages sorted by rust level (highest to lowest):")
for item in results:
    print(item)

#Top 5 using list slicing
print("\nTop 5 most rusted images:")
topFive = results[:5]
for item in topFive:
    print(item)

#Binary Search
targetLevel = 1

print("\nSearching for rust level: " + str(targetLevel))

if binarySearch(results, targetLevel):
    print("Images with rust level " + str(targetLevel) + ":")
    for item in results:
        if item[2] == targetLevel:
            print(item)
else:
    print("No images found with that rust level.")
