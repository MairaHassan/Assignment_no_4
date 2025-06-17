# subtract_program.py

from helpers import subtract_seven

def main():
    number = int(input("Enter a number: "))
    result = subtract_seven(number)
    print("Result after subtracting 7:", result)

if __name__ == "__main__":
    main()
