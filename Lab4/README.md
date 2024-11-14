# Lab Exercises

This lab will help you solidify your understanding of working with NumPy, Pandas, and GeoPandas for geospatial data analysis. Through these exercises, you will perform data manipulation, spatial analysis, and visualizations by combining these powerful libraries

Exercise 1: NumPy Array Operations and Geospatial Coordinates
In this exercise, you will work with NumPy arrays representing geospatial coordinates (latitude and longitude) and perform basic array operations.

Create a 2D NumPy array containing the latitude and longitude of the following cities: Tokyo (35.6895, 139.6917), New York (40.7128, -74.0060), London (51.5074, -0.1278), and Paris (48.8566, 2.3522).

Convert the latitude and longitude values from degrees to radians using np.radians().

Calculate the element-wise difference between Tokyo and the other cities’ latitude and longitude in radians.

Exercise 2: Pandas DataFrame Operations with Geospatial Data
In this exercise, you’ll use Pandas to load and manipulate a dataset containing city population data, and then calculate and visualize statistics.

Load the world cities dataset from this URL using Pandas: opengeos/datasets

Display the first 5 rows and check for missing values.

Filter the dataset to only include cities with a population greater than 1 million.

Group the cities by their country and calculate the total population for each country.

Sort the cities by population in descending order and display the top 10 cities.

Exercise 3: Creating and Manipulating GeoDataFrames with GeoPandas
This exercise focuses on creating and manipulating GeoDataFrames, performing spatial operations, and visualizing the data.

Load the New York City building dataset from the GeoJSON file using GeoPandas: opengeos/datasets

Create a plot of the building footprints and color them based on the building height (use the height_MS column).

Create an interactive map of the building footprints and color them based on the building height (use the height_MS column).

Calculate the average building height (use the height_MS column).

Select buildings with a height greater than the average height.

Save the GeoDataFrame to a new GeoJSON file.

Exercise 4: Combining NumPy, Pandas, and GeoPandas
This exercise requires you to combine the power of NumPy, Pandas, and GeoPandas to analyze and visualize spatial data.

Use Pandas to load the world cities dataset from this URL: opengeos/datasets

Filter the dataset to include only cities with latitude values between -40 and 60 (i.e., cities located in the Northern Hemisphere or near the equator).

Create a GeoDataFrame from the filtered dataset by converting the latitude and longitude into geometries.

Reproject the GeoDataFrame to the Mercator projection (EPSG:3857).

Calculate the distance (in meters) between each city and the city of Paris.

Plot the cities on a world map, coloring the points by their distance from Paris.
