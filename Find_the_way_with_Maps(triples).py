# Write a Python program to triple all numbers of a given list of integers. Use Python map.

# sample list: [1, 2, 3, 4, 5, 6, 7]

# Triple of list numbers:

# [3, 6, 9, 12, 15, 18, 21]


input_list = input("Enter list of int values : ")
input_list = input_list.split(",")
input_list = [int(i) for i in input_list]

def triple(l):
    return l*3

output_list = list(map(triple,input_list))
print("Triple of list numbers:",output_list)

# With lambda function 
print("\n************With Lambda Function*****************")

output_list1 = list(map(lambda x:x*3,input_list))
print("Triple of list numbers:",output_list1)
