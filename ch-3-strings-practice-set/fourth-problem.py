# Replace the double space from problem 3 with single space
# Code of third problem
required_string = "String with  double space"
# When double space is not present then it will return -1 and if it present then it will return the index
double_space = required_string.find('  ')
# find() function retuns the index of sub-string in the parent string
# returns -1 if substring is not found in parent string
# If found then it will return the index of substring in the parent string
print(required_string.replace("  "," "))
# String are immutable that means that original string does not change
# That means if I print(name) then still it prints the strings with double spaces
# Original strings does not change - That's why it is called immutable