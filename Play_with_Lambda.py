# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.

# sample input: 10
# sample output: 35


n=int(input(" Enter integer number: "))
add_25 = lambda x:x+25
print(" Output : ",add_25(n))
