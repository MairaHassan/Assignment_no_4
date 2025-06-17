def main():
    count = 0         # Track how many even numbers have been printed
    number = 0        # Start from 0

    while count < 20:
        print(number, end=' ')
        number += 2
        count += 1

if __name__ == "__main__":
    main()
