import random

# Global variable (used only to show scope, not recommended for real use)
total_rolls = 0

def roll_die():
    """Simulate rolling a die (1 to 6)."""
    roll = random.randint(1, 6)
    return roll

def roll_two_dice():
    """Roll two dice and print the results."""
    # Local variables
    die1 = roll_die()
    die2 = roll_die()
    print(f"Rolled: Die 1 = {die1}, Die 2 = {die2}")

def simulate_rolls():
    """Simulate rolling dice three times."""
    global total_rolls  # Access the global variable
    for i in range(3):
        print(f"\nRoll #{i + 1}")
        roll_two_dice()
        total_rolls += 1

# Entry point of the program
if __name__ == "__main__":
    simulate_rolls()
    print(f"\nTotal number of rolls: {total_rolls}")
