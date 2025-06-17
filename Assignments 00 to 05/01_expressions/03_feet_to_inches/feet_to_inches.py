def convert_feet_to_inches(feet):
    """Convert feet to inches."""
    return feet * 12

def main():
    print("Feet to Inches Converter")
    print("Enter 'q' to quit.\n")

    while True:
        user_input = input("Enter length in feet: ")

        if user_input.lower() == 'q':
            print("Goodbye!")
            break

        try:
            feet = float(user_input)
            inches = convert_feet_to_inches(feet)
            
            foot_label = "foot" if feet == 1 else "feet"
            print(f"\n{feet} {foot_label} is equal to {inches} inches.\n")
        except ValueError:
            print("Please enter a valid number or 'q' to quit.\n")

if __name__ == "__main__":
    main()
