# repeat_message.py

def print_multiple(message, repeats):
    """
    Prints the given message a specified number of times.

    Parameters:
        message (str): The message to print.
        repeats (int): Number of times to print the message.
    """
    for _ in range(repeats):
        print(message)

def main():
    message = input("Please type a message: ")
    try:
        repeats = int(input("Enter a number of times to repeat your message: "))
        print_multiple(message, repeats)
    except ValueError:
        print("Please enter a valid number.")

if __name__ == "__main__":
    main()
