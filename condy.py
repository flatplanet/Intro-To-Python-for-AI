import os
# Clear the screen
os.system("clear")

# Conditional Statements
# If, Else, Elif

num1 = 0
num2 = 1

if num1 > num2:
	print(f'Yes! {num1} is greater than {num2}')
elif  num1 == num2:
	print(f'{num1} equals {num2}')
else:
	print(f'No! {num1} is not greater than {num2}')
