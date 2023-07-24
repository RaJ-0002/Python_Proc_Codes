# Write a Python program to square the elements of a list using map() function.

# Sample List: [4, 5, 2, 9]

# Square the elements of the list:

# [16, 25, 4, 81]

input_list = input("Enter list of int values : ")
input_list = input_list.split(",")
input_list = [int(i) for i in input_list]

def square(l):
    return l**2

output_list = list(map(square,input_list))
print("Square of given list : ",output_list)

print("\n***********with lambda function***************")

output_list_2 = list(map(lambda x:x**2,input_list))
print("Square list with lambda : ",output_list_2)
