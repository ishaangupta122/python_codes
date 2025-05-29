# Original list with duplicates
my_list = [1, 2, 3, 2, 4, 1, 5, 3]

print("Original list:", my_list)

# Convert list to set to remove duplicates
my_set = set(my_list)
print("Set (duplicates removed):", my_set)

# Convert set back to list
unique_list = list(my_set)
print("List after removing duplicates:", unique_list)
