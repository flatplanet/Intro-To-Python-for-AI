import os
# Clear the screen
os.system("clear")

# Data Type
# Dictionaries - key:value pairs

fav_pizza = {
	"John":"Veggie",
	"April": "Supreme",
	"Bob":"Ham"
}

print(fav_pizza)

# Change and item
#fav_pizza["John"] = "Ham"

# Add an item
#fav_pizza.update({"Tina":"Cheese"})


# Remove an item
del fav_pizza["Bob"]
print(fav_pizza)
