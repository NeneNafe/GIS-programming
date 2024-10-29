# create a list of coordinates
# use a for loop to iterate over them
# Use an if-elif-else statement inside the loop to classify each
# coordinate based on its longitude

geographical_coordinates = [
    (55.7558, 37.6173),
    (19.4326, -99.1332),
    (37.5665, 126.9780),
    (-12.0464, -77.0428)
]

for lat, lon in geographical_coordinates:
    if lon > 0:
        print(f"Eastern Hemisphere")
    elif lon < 0:
        print(f"Western Hemisphere")
    else:
        print("No Coordinate found!")
