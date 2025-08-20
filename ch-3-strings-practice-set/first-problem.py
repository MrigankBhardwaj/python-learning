# Write a Python program to display a user entered name followed by Good Afternoon using input() function
input_string = input("Enter your name: ")
# print(input_string + " Good afternoon") # In Python to concat two strings you have to use the + sign

# We can do this usign f string also
print(f"Good afternoon {input_string}") # Remember to use the variable inside the string you have to make that string f string
# Without f string you can't use variable inside the string under curly braces