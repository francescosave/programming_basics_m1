
import re

user_input = input("Enter the input ")

num_format = re.compile(r'^\-?[1-9][0-9]*$')
isInteger = re.match(num_format,user_input)

if isInteger: print("True")
else: print("False")