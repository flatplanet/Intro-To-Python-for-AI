import os
# Clear the screen
os.system("clear")

# Data Type
# tuples
first_names = ("John", "April", "Bob")
print(first_names)

# change the tuple
first_names2 = ("Tina",)

# Create a new tuple with the old tuple info
first_names3 = first_names + first_names2

print(first_names3)

# Remove items
new_tuple = first_names[0:2]
print(new_tuple)