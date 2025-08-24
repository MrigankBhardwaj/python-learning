# Write a Python program to accept marks of 6 students and display them in a sorted manner
#  we will take multiple value in a single line
students_marks = []
student1 = int(input("Enter the marks of 1st student: "))
students_marks.append(student1)
student2 = int(input("Enter the marks of 2nd student: "))
students_marks.append(student2)
student3 = int(input("Enter the marks of 3rd student: "))
students_marks.append(student3)
student4 = int(input("Enter the marks of 4th student: "))
students_marks.append(student4)
student5 = int(input("Enter the marks of 5th student: "))
students_marks.append(student5)
student6 = int(input("Enter the marks of 6th student: "))
students_marks.append(student6)
# students_marks.extend(student1,student2,student3,student4,student5,student6)
students_marks.sort()
print(students_marks)
