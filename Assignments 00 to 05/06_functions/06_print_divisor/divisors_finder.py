# divisors_finder.py

def print_divisors(num):
    """
    Prints all divisors of the given number from 1 to num (inclusive).
    
    Parameters:
        num (int): The number whose divisors are to be printed.
    """
    print(f"Here are the divisors of {num}")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=' ')
    print()  # newline after all divisors are printed

def main():
    try:
        user_input = int(input("Enter a number: "))
        print_divisors(user_input)
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
