import os
# Clear the screen
os.system("clear")

# Classes
class Square():
	def __init__(self, side_length):
		self.side_length = side_length

	def area(self):
		# Area of a squre is side_length * side_length
		return self.side_length * self.side_length

	def perimeter(self):
		# Perimeter of a square is side_length * 4
		return self.side_length * 4
	def report(self):
		print(f"Side Length: {self.side_length}")
		print(f"Area: {self.area()}")
		print(f"Perimeter: {self.perimeter()}")

# Instantiate The Class
my_square = Square(10)

#print(my_square.side_length)
# Area
#print(f'Area: {my_square.area()}')
# Perimeter
#print(my_square.perimeter()) 
# Report
my_square.report()
