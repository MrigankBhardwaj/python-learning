# Write a Python program to print the contents of a directory using the os module
import os
"""
I am 
going to 
print all the content of any directory
"""
content = os.listdir(r"M:\A-Learn-Pyhton\ch-1-practice-set")  # Why to add 'r' - because the python interpreter doesn't treat backslashes as a special character and treat then as a raw string
print(content)
# Here both fouth and fifth practice set completes as fifth one is to label fourth problem with comments