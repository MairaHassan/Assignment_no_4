MIN_HEIGHT = 50  # Minimum height to ride

def tall_enough_extension():
    while True:
        height_input = input("How tall are you? ")
        
        # Exit if input is blank
        if height_input == "":
            print("Goodbye!")
            break

        try:
            height = int(height_input)
            if height >= MIN_HEIGHT:
                print("You're tall enough to ride!\n")
            else:
                print("You're not tall enough to ride, but maybe next year!\n")
        except ValueError:
            print("Please enter a valid number.\n")

if __name__ == "__main__":
    tall_enough_extension()
