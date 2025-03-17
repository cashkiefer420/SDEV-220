# Assign values to variables
guess_me = 7
number = 1

# While loop to compare number with guess_me
while number <= guess_me:
    if number < guess_me:
        print("too low")  # If number is less than guess_me
    elif number == guess_me:
        print("found it!")  # If number matches guess_me
        break  # Exit the loop
    number += 1  # Increment number

# If the loop exits naturally and number is greater than guess_me
if number > guess_me:
    print("oops")  # Number went past guess_me
