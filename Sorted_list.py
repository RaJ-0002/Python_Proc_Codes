# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples
#Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
#Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

sample_list = list()
sample_tuple = tuple()
length_of_list = int(input("Enter the length of list"))
for i in range(length_of_list):
    sample_tuple = input("Enter only 2 int tuple values")
    sample_tuple = sample_tuple.split(',')
    sample_tuple = [int(i) for i in sample_tuple]
    sample_tuple = tuple(sample_tuple)
    sample_list.append(sample_tuple)
print(sample_list)

sample_list.sort(key=lambda x: x[-1])
print(sample_list)
