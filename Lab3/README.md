# Lab 3 Exercises

Exercise 1: Calculating Distances with Functions
Define a function calculate_distance that takes two geographic coordinates (latitude and longitude) and returns the distance between them using the Haversine formula.

Use this function to calculate the distance between multiple pairs of coordinates.

Exercise 2: Batch Distance Calculation
Create a function batch_distance_calculation that accepts a list of coordinate pairs and returns a list of distances between consecutive pairs.

Test the function with a list of coordinates representing several cities.

Exercise 3: Creating and Using a Point Class
Define a Point class to represent a geographic point with attributes latitude, longitude, and name.

Add a method distance_to that calculates the distance from one point to another.

Instantiate several Point objects and calculate the distance between them.

Exercise 4: Reading and Writing Files
Write a function read_coordinates that reads a file containing a list of coordinates (latitude, longitude) and returns them as a list of tuples.

Write another function write_coordinates that takes a list of coordinates and writes them to a new file.

Ensure that both functions handle exceptions, such as missing files or improperly formatted data.

Exercise 5: Processing Coordinates from a File
Create a function that reads coordinates from a file and uses the Point class to create Point objects.

Calculate the distance between each consecutive pair of points and write the results to a new file.

Ensure the function handles file-related exceptions and gracefully handles improperly formatted lines.

- Create a sample coordinates.txt file
sample_data = """35.6895,139.6917
34.0522,-118.2437
51.5074,-0.1278
-33.8688,151.2093
48.8566,2.3522"""

output_file = "coordinates.txt"

try:
    with open(output_file, "w") as file:
        file.write(sample_data)
    print(f"Sample file '{output_file}' has been created successfully.")
except Exception as e:
    print(f"An error occurred while creating the file: {e}")
Sample file 'coordinates.txt' has been created successfully.
Exercise 6: Exception Handling in Data Processing
Modify the batch_distance_calculation function to handle exceptions that might occur during the calculation, such as invalid coordinates.

Ensure the function skips invalid data and continues processing the remaining data.
