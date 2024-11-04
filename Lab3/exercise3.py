# A Point class to represent a geog point
# Adds a method that calculates the distance from one point to another
# Instantiates several Point objects & calculate the distance between them


import sys
sys.path.append('/home/nenenafe/GIS-programming')

from Lab3.exercise1 import calculate_distance

class Point:
    def __init__(self, latitude, longitude, name=None):
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
        
    def distance_to(self, other_point):
        # Calculate the distance between several points
        return calculate_distance(
            self.latitude, self.longitude, other_point.latitude, other_point.longitude
            ) # Called the func calculate_distance, to find the distances
    
# Example Usage
point1 = Point(60.1695, 24.9354, 'Helsinki')
point2 = Point(52.5200, 13.4050, 'Berlin')
point3 = Point(48.8566, 2.3522, 'Paris')
print(f"The distance between {point1.name} and {point2.name} is {point1.distance_to(point2):.2f} km")
print(f"The distance between {point1.name} and {point3.name} is {point1.distance_to(point3):.2f} km")
