# Check the type of variable assigned using input() function
# First we take input and then check its type using type() function 
#  Please remember inout type is always string, if we want to change that we have use int(), float() like funcitons on input
input_variable = input("Enter the value: ") # Getting value - user input
type_of_input_variable =  type(input_variable) # Getting type of input using the type() method
print(type_of_input_variable) # printing that type of input - out wil be always <class 'str'> because input type by default is string