This first Lab comprises of 10 exercises where:

Exercise 1: Variable Assignment and Basic Operations
Create variables to store the following geospatial data:

The latitude and longitude of New York City: 40.7128, -74.0060.

The population of New York City: 8,336,817.

The area of New York City in square kilometers: 783.8.

Perform the following tasks:

Calculate and print the population density of New York City (population per square kilometer).

Print the coordinates in the format “Latitude: [latitude], Longitude: [longitude]”.

Exercise 2: Working with Strings
Create a string variable to store the name of a city, such as “San Francisco”. Perform the following operations:

Convert the string to lowercase and print the result.

Convert the string to uppercase and print the result.

Replace “San” with “Los” in the city name and print the new string.

Exercise 3: Using Lists
Create a list of tuples, where each tuple contains the name of a city and its corresponding latitude and longitude:

New York City: (40.7128, -74.0060)

Los Angeles: (34.0522, -118.2437)

Chicago: (41.8781, -87.6298)

Perform the following tasks:

Add a new city (e.g., Miami: (25.7617, -80.1918)) to the list.

Print the entire list of cities.

Slice the list to print only the first two cities.

Exercise 4: Using Tuples
Create a tuple to store the coordinates (latitude, longitude) of the Eiffel Tower: (48.8584, 2.2945). Perform the following tasks:

Access and print the latitude and longitude values from the tuple.

Try to change the latitude value to 48.8585. What happens? Explain why.

Exercise 5: Working with Sets
Create a set of countries you have visited, such as {“USA”, “France”, “Germany”}. Perform the following tasks:

Add a new country to the set.

Try to add the same country again. What happens?

Print the updated set.

Exercise 6: Working with Dictionaries
Create a dictionary to store information about a specific geospatial feature, such as a river:

Name: “Amazon River”

Length: 6400 km

Countries: [“Brazil”, “Peru”, “Colombia”]

Perform the following tasks:

Add a new key-value pair to the dictionary to store the river’s average discharge (e.g., 209,000 m³/s).

Update the length of the river to 6992 km.

Print the dictionary.

Exercise 7: Nested Data Structures
Create a dictionary to represent a city that contains the city’s name, population, and coordinates (latitude, longitude):

Name: “Tokyo”

Population: 13,515,271

Coordinates: (35.6895, 139.6917)

Perform the following tasks:

Access and print the population of the city.

Access and print the city’s latitude.

Update the population to 14,000,000 and print the updated dictionary.

Exercise 8: List Operations
Given the list of cities from Exercise 3, perform the following operations:

Sort the list of cities alphabetically by name.

Create a new list that contains only the city names.

Remove the last city from the original list and print the updated list.

Exercise 9: Dictionary Operations
Using the dictionary from Exercise 6, perform the following tasks:

Check if the key “Length” exists in the dictionary.

Print all the keys in the dictionary.

Print all the values in the dictionary.

Exercise 10: Practical Application
Imagine you have a list of tuples, each representing a location with its name, latitude, and longitude:

locations = [
    ("Mount Everest", 27.9881, 86.9250),
    ("K2", 35.8808, 76.5155),
    ("Kangchenjunga", 27.7025, 88.1475),
]
Perform the following tasks:

Create a new list that contains only the names of the locations.

Create a dictionary where the keys are location names and the values are tuples of their coordinates.

Print the latitude of “K2” using the dictionary.