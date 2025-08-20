#   Write a program to detect double space in a string
required_string = "String with double space  "
# When double space is not present then it will return -1 and if it present then it will return the index
double_space = required_string.find('  ')
# find() function retuns the index of sub-string in the parent string
# returns -1 if substring is not found in parent string
# If found then it will return the index of substring in the parent string
print(double_space)