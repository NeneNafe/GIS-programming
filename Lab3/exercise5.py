# A function that reads coordinates from a file and uses
# the Point class to create Point objects
# Computes the distance between each consecutive pair of points
# and write the results to a new file
# Func handles file-related exceptions and improperly formatted lines

from math import radians, sin, cos, sqrt, atan2

class Point:
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
    
    def __repr__(self):
        return f"Point({self.latitude}, {self.longitude})"
 
   
def read_coordinates(read_file):
    coordinates = []
    
    try:
        with open(read_file, "r") as file:
            for line in file:
                # Checks every line in the file
                contents = line.strip().split(",") # Removes any spaces and separates the contents by comma  
                if len(contents) != 2:
                    # Checks if the number of coordinates is equal to 2
                    raise ValueError("Invalid number of coordinates")
                
                lat, lon = float(contents[0]), float(contents[1])
                coordinates.append((lat, lon))
    
    # Handles all the exceptions            
    except FileNotFoundError:
        print(f"Error: The file {read_file} was not found")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
    
    return coordinates


def calculate_distance(lat1, lon1, lat2, lon2):
    # a function that takes two args and calculates the distance between points
    radius = 6371.0
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 -lon1)
    
    haversine = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    ) # The Haversine function used to compute the distance between two points
    c = 2 * atan2(sqrt(haversine), sqrt(1 - haversine))
    
    distance = radius * c
    
    return distance # Returns the distance between two points


def write_distances(coordinates, write_files):
    # A function that writes the distance between two points to a file
    try:
        with open(write_files, "w") as file:
            for i in range(len(coordinates) - 1):
                lat1, lon1 = coordinates[i] # The first point
                lat2, lon2 = coordinates[i + 1] # The second point
                distance = calculate_distance(lat1, lon1, lat2, lon2) # The distance between the two points
                file.write(
                    f"From ({lat1}, {lon1}) to ({lat2}, {lon2}), The Distance is: {distance:.2f} km\n"
                    )
    except FileNotFoundError:
        print(f"Error: The file {write_files} was not found")
        
    except Exception as e:
        print(f"An error occurred: {e}")
        

# Example usage
coordinates = read_coordinates("coordinates.txt")
write_distances(coordinates, "distances.txt")
