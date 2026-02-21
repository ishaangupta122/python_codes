desired_numbers = []
for number in range(2000, 2501):
    if number % 7 == 0 and number % 5 != 0:
        desired_numbers.append(number)
        
print(f"Numbers b/w 2000 and 2500 that are not multiple of 5: ")
print(desired_numbers)  