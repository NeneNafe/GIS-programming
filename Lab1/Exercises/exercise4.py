# Create a tuple to store the coordinates (latitude, longitude) of the Eiffel Tower

Eiffel_Tower = (48.8584, 2.2945)

# Access and print the latitude and longitude values from the tuple
print(f"The Latitude of the Eiffel Tower is {Eiffel_Tower[0]}, and the Longitude of the Eiffel Tower is {Eiffel_Tower[1]}")

Eiffel_Tower[0] = 48.8585

print(Eiffel_Tower) # This will throw an error because tuples are immutable