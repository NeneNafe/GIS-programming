# Building dynamic SQL queries
# given a table name and a condition
# Add additional conditions dynamically, like AND clauses

table_name = "cities" # table name
condition = "population > 1000000" # condition
additional_conditions = "area < 1500m2" # additional condition

sql_query = f"SELECT * FROM {table_name} WHERE {condition} AND {additional_conditions}"
print(sql_query)
