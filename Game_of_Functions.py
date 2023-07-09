#Write a Python function to sum all the numbers in a list.
#Sample List : (8, 2, 3, 0, 7)
#Expected Output : 20
#Explanation:
#Summation should like 8+2+3+0+7 = 20

input_list = input("Enter int values : ")
input_list = input_list.split(",")
input_list = [int(i) for i in input_list]
total = 0

def Sum_num(numbers):
    global total
    for num in numbers:
        total +=num
        if numbers[-1]==num:
            print(num,end=" ")
        else:
            print(num,"+ ",end="")
    return total

print("=",Sum_num(input_list))
