# A function that reads a file containing a list of coordinates
# returns a list of tuples
# another function that takes a list of coordinate and writes to a new file
# Both functions handle exceptions

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


def write_coordinates(file_name, coordinates):
    # Takes the list from the function above and writes it to a new file
    try:
        with open(file_name, "w") as file:
            for lat, lon in coordinates: # Unpacks the tuple
                file.write(f"Latitude: {lat}, Longitude: {lon}\n")
                
    except FileNotFoundError:
        print(f"Error: The {file_name} is missing")
        
    except Exception as e:
        print(f"An error occurred: {e}")


# Example usage
coordinates = read_coordinates("geog_coordinates.txt")
write_coordinates("new_coordinates.txt", coordinates)
