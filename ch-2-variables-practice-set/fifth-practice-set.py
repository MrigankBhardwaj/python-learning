# Write a Pyhton program to find an average of two numbers entered by the users
# Used int() method because by default input method only gives string .. and to find the average you need integers not strings
first_input_number = int(input("Enter first number: "))
second_input_number =  int(input("Enter second number: "))
sum_of_both_numbers = first_input_number + second_input_number
average_of_both_number = sum_of_both_numbers / 2
print(average_of_both_number)