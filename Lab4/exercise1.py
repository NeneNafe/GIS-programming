import numpy as np # type: ignore

# A 2D NumPy array with geo coordinates
# Convert lat and lon to radians
# Calculate the element-wise diff between Tokyo &
# other Cities' lat and lon in radians

city_array = np.array([
    [35.6895, 139.6917], 
    [40.7128, -74.0060], 
    [51.5074, -0.1278], 
    [48.8566, 2.3522]
])

# Convert lat and lon to radians
city_array_radians = np.radians(city_array)

np.set_printoptions(precision=4, suppress=True)

# Calculate the element-wise diff between Tokyo &
# other Cities' lat and lon in radians
elem_wise_diff = city_array_radians - city_array_radians[0]

print(f"The 2D NumPy array with geo coordinates is: \n{city_array}")

print(f"The array in radian is: \n{city_array_radians}")

print(f"The element-wide different between Tokyo and the other cities is: \n{elem_wise_diff}")