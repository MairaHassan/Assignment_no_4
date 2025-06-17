from number_generator import generate_number

print("I am thinking of a number between 0 and 99...")

secret = generate_number()
guess = None

while guess != secret:
    guess = int(input("Enter a guess: "))
    
    if guess < secret:
        print("Your guess is too low")
    elif guess > secret:
        print("Your guess is too high")
    else:
        print(f"Congrats! The number was: {secret}")
