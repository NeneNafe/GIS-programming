# Lab 2 Exercises

## Exercise 1: Manipulating Geographic Location Strings

Create a string that represents the name of a geographic feature (e.g., "Amazon River").

Convert the string to lowercase and then to uppercase.

Concatenate the string with the name of the country (e.g., "Brazil") to create a full location name.

Repeat the string three times, separating each repetition with a dash (-).

Exercise 2: Extracting and Formatting Coordinates
Given a string with the format "latitude, longitude" (e.g., "40.7128N, 74.0060W"), extract the numeric values of latitude and longitude.

Convert these values to floats and remove the directional indicators (N, S, E, W).

Format the coordinates into a POINT WKT string (e.g., "POINT(-74.0060 40.7128)").

Exercise 3: Building Dynamic SQL Queries
Given a table name and a condition, dynamically build an SQL query string.

Example: If table_name = "cities" and condition = "population > 1000000", the query should be "SELECT * FROM cities WHERE population > 1000000;".

Add additional conditions dynamically, like AND clauses.

Exercise 4: String Normalization and Cleaning
Given a list of city names with inconsistent formatting (e.g., [" new york ", "Los ANGELES", "   CHICAGO"]), normalize the names by:

Stripping any leading or trailing whitespace.

Converting them to title case (e.g., "New York", "Los Angeles", "Chicago").

Ensure that the output is a clean list of city names.

Exercise 5: Parsing and Extracting Address Information
Given a string in the format "Street, City, Country" (e.g., "123 Main St, Springfield, USA"), write a function that parses the string into a dictionary with keys street, city, and country.

The function should return a dictionary like {"street": "123 Main St", "city": "Springfield", "country": "USA"}.
