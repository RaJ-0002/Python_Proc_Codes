#Write a Python program to reverse a string.

#﻿Sample String : "1234abcd"
#Expected Output : "dcba4321"

def reverse_str(string):
    reversed_string = ""
    for char in string[::-1]:
        reversed_string += char
    return reversed_string

input_str = input("Enter the input string: ")
output = reverse_str(input_str)
print("Output :", output)
