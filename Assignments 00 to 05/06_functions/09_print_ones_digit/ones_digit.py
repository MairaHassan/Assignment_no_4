# ones_digit.py

def print_ones_digit(num):
    """
    Prints the ones digit of the given integer.
    
    Parameters:
        num (int): The number to extract the ones digit from.
    """
    ones_digit = abs(num) % 10
    print(f"The ones digit is {ones_digit}")

def main():
    try:
        user_input = int(input("Enter a number: "))
        print_ones_digit(user_input)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
