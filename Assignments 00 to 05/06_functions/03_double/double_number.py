# double_number.py

def double(num):
    """
    Returns double the input number.

    Parameters:
        num (int or float): The number to double.
    
    Returns:
        int or float: The doubled number.
    """
    return num * 2


def main():
    user_input = input("Enter a number: ")
    try:
        number = float(user_input) if '.' in user_input else int(user_input)
        result = double(number)
        print(f"Double that is {result}")
    except ValueError:
        print("That's not a valid number.")


if __name__ == "__main__":
    main()
