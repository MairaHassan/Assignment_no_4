# Constant for speed of light in meters per second
C = 299792458  # m/s

def calculate_energy(mass):
    """Calculate energy using Einstein's equation."""
    return mass * (C ** 2)

def main():
    print("Mass to Energy Converter (Einstein's E = mc^2)")
    print("Enter 'q' to quit.\n")

    while True:
        user_input = input("Enter kilos of mass: ")

        if user_input.lower() == 'q':
            print("Exiting the program.")
            break

        try:
            mass = float(user_input)
            print("\ne = m * C^2...\n")
            print(f"m = {mass} kg")
            print(f"C = {C} m/s")

            energy = calculate_energy(mass)
            print(f"{energy} joules of energy!\n")
        except ValueError:
            print("Please enter a valid number or 'q' to quit.\n")

if __name__ == "__main__":
    main()
