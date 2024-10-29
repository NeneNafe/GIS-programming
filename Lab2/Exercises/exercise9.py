# Filter out a list of coordinates and store only those located
# in the Southern Hemisphere
# Count the number of coordinates that meet the condition

geographical_coordinates = [
    (55.7558, 37.6173),
    (19.4326, -99.1332),
    (37.5665, 126.9780),
    (-12.0464, -77.0428)
]

filtered_data = []
index = 0
for lat, lon in geographical_coordinates:
    if lat < 0:
        filtered_data.append((lat, lon))
        index += 1
print(
    f"The filtered data based on the condition: ({lat}, {lon}.\nThe number of the coordinates in the South Hemisphere: {index}"
    )