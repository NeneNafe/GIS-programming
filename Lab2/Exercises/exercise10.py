# a program that generates random coordinates
# (latitude between [-90, 90] degrees and longitude between [-180, 180] degrees)

import random

while True: # The condition that generates the random coordinates
    lat = random.uniform(-90, 90) # the range of the random generated latitudes
    lon = random.uniform(-180, 180) # the range of the random generated longitudes
    print(f"The Random generated coordinates are: ({lat:.4f}, {lon:.4f})")
    # Print to 4 Decimal places
    if lat > 50 and lon > 50: # The condition to stop generating the coordinates
        break
