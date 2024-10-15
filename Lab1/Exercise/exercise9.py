# Checks if the "Length" exists in the dictionary
# Print all the keys in the dictionary
# Print all the values in the dictionary

geo_feature = {
    "Name": "Amazon River",
    "Length": "6400 km",
    "Countries": ["Brazil", "Peru", "Colombia"]
}

if "Length" in geo_feature:
    print("Length exists in the dictionary")
else:
    print("Length does not exist in the dictionary")

print("Keys in the dictionary are:")
for key in geo_feature:
    print(key)
else:
    print(None)
    
print("Values in the dictionary are:")
for value in geo_feature:
    print(geo_feature[value])