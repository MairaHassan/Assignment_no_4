# even_odd_labeler.py

def even_odd_labels(start, end):
    """
    Prints numbers from start to end (inclusive) with 'even' or 'odd' labels.

    Parameters:
        start (int): Starting number.
        end (int): Ending number.
    """
    for num in range(start, end + 1):
        label = "even" if num % 2 == 0 else "odd"
        print(f"{num} {label}", end=' ')
    print()  # For a newline after the loop

def main():
    even_odd_labels(10, 19)

if __name__ == "__main__":
    main()
