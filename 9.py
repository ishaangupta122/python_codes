def is_palindrome(input_string):
    cleaned_string = input_string.replace("", " ").lower()
    reversed_string = cleaned_string[::-1]
    return cleaned_string == reversed_string

example_string = "A man a plan a canal panama"
if is_palindrome(example_string):
    print(f'"{example_string}" is a palindrome.')
else:
    print(f'"{example_string}" is not a palindrome.')