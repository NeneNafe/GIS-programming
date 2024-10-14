# Create a string varibale to store the name of a city, such as San Franciso
# Convert the stirng to lowercase and print the result
# Replace "San" with "Los" in the city name and print the result

city_name = "San Francisco"

city_name = city_name.lower()
print(city_name)

city_name = city_name.upper()
print(city_name)

city_name = city_name.split()
city_name[0] = "Los"
city_name = " ".join(city_name)
print(city_name)