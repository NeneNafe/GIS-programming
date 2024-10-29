# Create a list of coordinates
# Write a while loop that prints each coordinate until
# it encounters a coordinate with a negative latitude

geographical_coordinates = [
    (55.7558, 37.6173),
    (19.4326, -99.1332),
    (37.5665, 126.9780),
    (-12.0464, -77.0428)
]

index = 0
while index < len(geographical_coordinates):
    # Measures the index against the total number of tuples in the list
    lat, lon = geographical_coordinates[index] # checks the coordinates on that index
    if lat < 0: # The condition that checks what is in the individual tuple
        break
    index += 1 # The index now increases after ever run and then print
    print(
        f"These are coordinates whose Latitude is greater than zero: ({lat}, {lon})"
        )
