# Assign value to guess_me
guess_me = 5

# Loop through numbers from 0 to 9
for number in range(10):
    if number < guess_me:
        print("too low")  # If number is less than guess_me
    elif number == guess_me:
        print("found it!")  # If number matches guess_me
        break  # Exit the loop
    else:
        print("oops")  # If number is greater than guess_me
        break  # Exit the loop
