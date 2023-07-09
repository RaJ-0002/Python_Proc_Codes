#Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.
#Sample String : 'The quick Brow Fox'
#Expected Output :
#No. of Upper case characters : 3
#No. of Lower case Characters : 12


def calculate(string):
    upper_count = 0
    lower_count = 0
    
    for char in string:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count +=1
    
    return upper_count, lower_count

input_str = input("Enter a string with combination of capital letters and small letters : ")
upper, lower = calculate(input_str)
print("No. of Upper case characters:", upper)
print("No. of Lower case Characters:", lower)
