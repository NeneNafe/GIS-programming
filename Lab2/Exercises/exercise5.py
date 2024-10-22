# parsing and extracting data from a file
# a function that parses the str into a dictionary with keys

def str_to_dict(string):
    keys = string.split(", ")
    values = ["123 Main St", "Springfield", "USA"]
    str_to_dict = dict(zip(keys, values))
    
    print(str_to_dict)
    
str_format = "Street, City, Country"
str_to_dict(str_format)
