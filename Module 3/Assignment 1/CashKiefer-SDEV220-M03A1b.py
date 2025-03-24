# Defining the function that returns the list of names
def good():
    return ["Harry", "Ron", "Hermione"]

# Calling the function and printing the result
print(good())

# Defining the generator function that yields odd numbers from range(10)
def get_odds():
    for num in range(10):
        if num % 2 == 1:  # Checking if the number is odd
            yield num  # Yielding the odd number

# Using a for loop to get the third odd number
count = 0
for odd in get_odds():
    count += 1
    if count == 3:  # Stopping at the third odd number
        print("The third odd number is:", odd)
        break
