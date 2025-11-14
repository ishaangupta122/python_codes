print('Case 1:')
a=5
b=10
print(f"original values: a = {a}, b = {b}")
temp = a
a = b
b = temp
print(f"swapped values: a = {a}, b = {b}")

print('Case 2:')
a=5
b=10
print(f"original values: a = {a}, b = {b}")
a, b = b, a 
print(f"swapped values: a = {a}, b = {b}")