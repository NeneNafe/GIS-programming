# List Operations
# Sort the list alphabetically by name
# Create a new list that conatins only the cities
# Remove the last city from the list and print the updated list

list_of_cities = [("New York City", 40.7128, -74.0060),
                  ("Los Angeles", 34.0522, -118.2437),
                  ("Chicago", 41.8781, -87.6298)]

original_list = list_of_cities.copy() # Copy the list to keep the original list

list_of_cities.sort() # Sort the list alphabetically by name
print(list_of_cities)

city_names = [city_name[0] for city_name in list_of_cities]
print(city_names)

original_list.pop() # Remove the last city from the list
print(original_list)