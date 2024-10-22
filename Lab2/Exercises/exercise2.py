# Extract numeric values of a string
# convert these values to floats and remove directional indicators
# format the coordinates into a POINT WKT string

coordinate_strings = "40.7128N, 74.0060W"
latitude, longitude = coordinate_strings.split(", ")# split the string into latitude and longitude
print(latitude, longitude)

# remove the directional indicators and convert the values to floats
latitude = float(latitude[:-1])
longitude = float(longitude[:-1])
print(latitude, longitude)

# create a POINT WKT string
wtk_point = f"POINT({longitude} {latitude})"
print(wtk_point)