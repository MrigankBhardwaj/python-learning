# Write a Python program to fill in a letter given below wiht name and date
import datetime
letter = """
    Dear <|Name|>,
    You are selected!
    <|Date|>
    ...
"""
name = input("Enter your name: ")
today = datetime.date.today()
today_date = today.strftime("%d-%m-%y")
# print(type(today_date))
replaced_name = letter.replace("<|Name|>", name)
replaced_date = replaced_name.replace("<|Date|>",today_date)
print(replaced_date)
