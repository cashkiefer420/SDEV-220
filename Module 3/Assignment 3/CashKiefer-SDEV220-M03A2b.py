# Define the list with some numbers
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use lambda function with filter to select odd numbers
new_list = list(filter(lambda x: x % 2 != 0, my_list))

# Print the new list with odd numbers
print(new_list)
