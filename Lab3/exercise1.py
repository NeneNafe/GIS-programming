# A function that takes two geographic coordinates
# Returns the distance between them using the Haversine formula
# Calculates the distance between multiple pairs of coordinates

from math import radians, sin, cos, sqrt, atan2

def calculate_distance(lat1, lon1, lat2, lon2):
    # a function that takes two args
    radius = 6371.0
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 -lon1)
    
    haversine = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    )
    c = 2 * atan2(sqrt(haversine), sqrt(1 - haversine))
    distance = radius * c
    return distance

# example usage
distance = calculate_distance(35.6895, 139.6917, 37.7749, 122.4194)
print(f"The Distance is: {distance:.2f} km")
