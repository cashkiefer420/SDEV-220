# Assign a secret number between 1 and 10
secret = 7  

# Assign a guessed number between 1 and 10
guess = 5  

# Conditional tests to compare guess with secret
if guess < secret:
    print("too low")  # Guess is less than secret
elif guess > secret:
    print("too high")  # Guess is greater than secret
else:
    print("just right")  # Guess matches secret
