# String Normalization and Cleaning
# The output should be a list of city names

city_names = [" new york ", "Los ANGELES", "   CHICAGO"]

clean_city_names = [city.strip().title() for city in city_names]
print(clean_city_names)