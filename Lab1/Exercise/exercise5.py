# Create a set of countries you have visited
# Since i've never been to any other country,
# I will create a set of countries I would like to visit

wishlist = ["United Kingdom", "United States", "South Korea", "China", "Japan", "South Africa", "Australia",
            "New Zealand", "Canada", "Germany"]

wishlist = set(wishlist)
wishlist.add("Nigeria") # Add Nigeria to the set
print(wishlist)

wishlist.add("Nigeria") # Add Nigeria to the set again to see what happens
print(wishlist) # Nigeria is not added again because sets do not allow duplicates
