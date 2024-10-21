# Creates variables that store geo-cordinates
# Calculate and print the population density of New York City
# Print the coordinates in the format “Latitude: [latitude], Longitude: [longitude]”

latitude = 40.7128
longitude = -74.0060
population = 8336817
area_km2 = 783.8

New_York_City = (population / area_km2)

print("The population density of New York City per square kilometer is ", 
    New_York_City,"km2")
print("New York City lies at a latitude of", latitude, "and a longitude of", longitude)

print(f"Latitude: {[latitude]}, Longitude: {[longitude]}")