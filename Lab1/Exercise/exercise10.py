# A function that takes a list of tuples, each representing a location with
# its name, latitude, and longitude

locations = [
    ("Mount Everest", 27.9881, 86.9250),
    ("K2", 35.8808, 76.5155),
    ("Kangchenjunga", 27.7025, 88.1475),
]

# Create a new list that contains only the names of the locations
def names_of_locations(locations):
    return [location[0] for location in locations]

print(names_of_locations(locations))

# Create a dictionary where the keys are location names and
# the values are tuples of their coordinates
def local_dictionary(locations):
    return {location[0]: (location[1], location[2]) for location in locations}

print(local_dictionary(locations))

# Print the latitude for "K2" using the dictionary
print(dict(local_dictionary(locations))["K2"][0])