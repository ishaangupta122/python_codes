def myReverse(input_string):
    reversed_string = input_string[::-1]
    return reversed_string

original_string = str(input("Enter string: "))
reversed_string = myReverse(original_string)

print("Original string:", original_string)
print("Reversed string:", reversed_string)