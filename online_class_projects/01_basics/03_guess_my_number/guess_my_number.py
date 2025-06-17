import random

# Randomly choose a number between 0 and 99
secret_number = random.randint(0, 99)

# Ask the user for their first guess
guess = int(input("I am thinking of a number between 0 and 99... Enter a guess: "))

# Loop until the correct number is guessed
while guess != secret_number:
    if guess > secret_number:
        print("Your guess is too high")
    else:
        print("Your guess is too low")
    
    # Ask for another guess
    guess = int(input("Enter a new number: "))

# Correct guess
print(f"Congrats! The number was: {secret_number}")
