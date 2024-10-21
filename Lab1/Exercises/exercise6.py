# Create a dictionary to store information about a specific geospatial feature
# such as a river

geo_feature = {
    "Name": "Amazon River",
    "Length": "6400 km",
    "Countries": ["Brazil", "Peru", "Colombia"]
}

# Adds a new key-value pair to the dictionary to store the river's average discharge
geo_feature["Average Discharge"] = "209,000 m³/s"

# Updates the Length of the river
geo_feature["Length"] = "6992 km"

print(geo_feature)