## Rust Level Classification
To make searching easier and avoid issues with exact decimal values, rust percentages are grouped into four rust levels.
0–10%, Rust level 1, No or very little rust 
10–30%, Rust level 2, Light rust 
30–60%, Rust level 3, Medium rust 
60% or more, Rust level 4, Heavy rust 

Each image stores:
- The filename  
- The rust percentage  
- The rust level  


## Algorithms Used

### Selection Sort
Selection Sort is used to organize the images from the most rusted to the least rusted.  
The algorithm looks through the list, finds the image with the highest rust level, and moves it to the correct position.

Selection Sort was chosen because it is easy to understand, uses nested loops, and meets the Unit 6 requirements.


### Binary Search
Binary Search is used to check if any images have a specific rust level.  
Because the list is already sorted, Binary Search can quickly determine whether that rust level exists.

If more than one image has the same rust level, a simple loop is used to print all images that match.


## Performance Profiling
The program uses the time module to measure how long it takes to process all images.  
The total time is printed in seconds.

Most of the runtime comes from scanning every pixel in each image.


## Testing
- Images with no rust, some rust, and heavy rust were tested.  
- Images that visually looked more rusty had higher rust levels.  
- Sorting was checked to make sure the most rusted images appeared first.  
- Binary Search was tested using different rust levels.  

All tests worked as expected.


## Challenges Faced
- One challenge was comparing exact rust percentages when searching.  
- This was solved by grouping rust percentages into rust levels.

- Another challenge was showing more than one image with the same rust level.  
- This was solved by using a loop to print all matching images.

- And finally, Unidentified Image errors occured throughout coding the project, meaning multiple images had to be replaced.


## How To Run It
1. Open a Python IDE.  
2. Save the program as main.py.  
3. Make sure the image folder path is correct.  
4. Run the program.  
5. Boom! Check the results in the console.


## Conclusion
This project shows how simple image analysis can be used to solve real-life problems.  
By using pixel checking, sorting, and searching, the program compares rust levels across multiple images in a clear and effective way.
