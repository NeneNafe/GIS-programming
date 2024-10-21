 # Create a string that represents the name of a geographic feature
 # Convert the string to lowercase and then to uppercase
 # Concatenate the string with the name of the country (e.g., "Brazil")
 # to create a full location name
 # Repeat the string three times, separating each repetition with a dash (-)
 
geog_feature = "Shire River"
location = "Malawi"

print(geog_feature.lower())

print(geog_feature.upper())

geog_location = geog_feature + ", " + location # Concatenate the 2 strings

print(geog_location)

repeated_prints = (geog_feature + " - ") * 3

print(repeated_prints)