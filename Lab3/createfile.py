# Create a sample of coordinates.txt file
data = """-1.2863, 36.8172
35.6895, 139.6917
55.7558, 37.6176
37.7749, 122.4194
40.7128, 74.0060"""

output_file = "geog_coordinates.txt"

try:
    with open(output_file, "w") as file:
        file.write(data)
    print(f"The sample file {output_file} has been created")
except Exception as e:
    print(f"An error occurred while creating the file: {e}")
