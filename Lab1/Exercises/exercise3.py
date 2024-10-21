# Create a list of tuples, where each tuple contains the name of
# a city and its corresponding latitude and longitude

list_of_cities = [("New York City", 40.7128, -74.0060),
                  ("Los Angeles", 34.0522, -118.2437),
                  ("Chicago", 41.8781, -87.6298)]

# Adds a new city to the list
list_of_cities.append(("Miami", 25.7617, -80.1918))

# Prints the list of cities
print(list_of_cities)

# slices the list to prints only the first two cities
print(list_of_cities[:2])
