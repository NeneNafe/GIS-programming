# A list of tuples containing coordinates
# Determine whether the coordinate is from the North pr South Pore

list_of_coordinates = [
    (40.7128, 74.0060),
    (48.8566, 2.3522),
    (-35.6895, 139.6917),
    (30.0444, 31.2357),
    (-33.9249, 18.4241)
]

for lat, lon in list_of_coordinates:
    if lat > 0:
        hemisphere = "Northern"
    else:
        hemisphere = "Southern"
    print(f"The Coordinate ({lat}, {lon}) is in the {hemisphere} Hemisphere")
