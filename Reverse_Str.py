#Write a Python program that accepts a word from the user and reverse it.

#Sample Test Case
#Input : Edyoda
#output: adoydE


word = input("Input:")
reversed_word = ''

index = len(word) - 1
while index >= 0:
    reversed_word += word[index]
    index -= 1
print("Output:", reversed_word)
