import os
# Clear the screen
os.system("clear")

# For Loops!
names = ["John", "April", "Bob"]
name = "John Elder"
fav_pizza = {
	"John":"Veggie",
	"April":"Supreme",
	"Bob":"Ham",
}
for key,value in fav_pizza.items():
	print(f'{key} like {value} pizza')
