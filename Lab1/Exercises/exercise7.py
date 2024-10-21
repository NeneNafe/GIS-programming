# A dictionary to represent a city that contains the city’s
# name, population, and coordinates (latitude, longitude)

city_data ={
    "Name": "Tokyo",
    "Population": "13,515,271",
    "Coordinates": (35.6895, 139.6917)
}

print(city_data["Population"]) # Access the population of the city

print(city_data["Coordinates"][0]) # Access the latitude of the city

city_data["Population"] = "14,000,000" # Update the population of the city

print(city_data) # Print the updated city data
