# A function that accepts a list of coordinate pairs
# Handle exceptions during calculations such as invalid coordinates and
# Skips the invalid data & continues processing the data
# Returns a list of distances between consecutive pairs

import sys
sys.path.append('/home/nenenafe/GIS-programming')


from Lab3.exercise1 import calculate_distance

def batch_distance_calculation(coord_pairs):
    # a function that takes a list of coordinate pairs
    distances = []

    for i in range(len(coord_pairs) - 1):
        try:  
            lat1, lon1 = coord_pairs[i] # The first pair
            lat2, lon2 = coord_pairs[i + 1] # The second pair and on ...
            distance = calculate_distance(lat1, lon1, lat2, lon2)
            distances.append(distance)
        except (ValueError, TypeError) as e:
            continue
            
    if len(coord_pairs) < 2:
        raise ValueError("Invalid number of coordinates")
    
    return distances

# example Usage
coordinates = [(35.6895, 139.6917), (37.7749, 122.4194), (40.7128, 74.0060), ("invalid", "data")]
distances = batch_distance_calculation(coordinates)
formatted_distances = [round(dist, 2) for dist in distances]
print(f"The Distances between the coordinates are: {formatted_distances} km")
