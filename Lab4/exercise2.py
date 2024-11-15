import pandas as pd  # type: ignore

# A csv file of world cities dataset
# Display the first 5 rows and check for missing values
# Group the cities by their country & calculate the total
# population of each country
# Sort the cities by population in descending order
# display the first 10 cities

url = "https://github.com/opengeos/datasets/releases/download/world/world_cities.csv"
df = pd.read_csv(url)

# Filters the dataset to include cities with population greater than 1,000,000
filtered_pop = df[df["population"] > 1000000]

# Groups cities by their countries calc total pol for each country
grouped_cities = df.groupby("country")["population"].sum()

# Sorts the cities by population in descending order
sorted_cities = df.sort_values(by="population", ascending=False)


print(f"The first 5 rows of the cities:\n{df.head()}")  # Prints the first 5 rows
print(f"Cities with the population greater than 1 Million:\n{filtered_pop}") # Prints the cities with population greater than 1,000,000
print(f"The total population of each country:\n{grouped_cities}") # Prints the total population of each country
print(f" The 10 sorted cities by the their population is:\n{sorted_cities.head(10)}")
