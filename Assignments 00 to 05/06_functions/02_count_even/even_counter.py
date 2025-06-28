# even_counter.py

def count_even(lst):
    """
    Counts and prints the number of even integers in the given list.
    
    Parameters:
        lst (list of int): A list of integers.
    """
    even_count = sum(1 for num in lst if num % 2 == 0)
    print(f"Number of even numbers: {even_count}")


def main():
    lst = []
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        if user_input == "":
            break
        try:
            num = int(user_input)
            lst.append(num)
        except ValueError:
            print("That's not a valid integer. Please try again.")

    count_even(lst)


if __name__ == "__main__":
    main()
