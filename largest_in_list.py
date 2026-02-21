def largest(number):
    max_number = number[0]
    for i in number:
        if i > max_number:
            max_number = i   
    return max_number

user_input = input("Enter list of numbers separated by spaces: ")
numbers_list = list(map(int, user_input.split()))
largest_number = largest(numbers_list)  
print("The largest number in this list is:", largest_number)