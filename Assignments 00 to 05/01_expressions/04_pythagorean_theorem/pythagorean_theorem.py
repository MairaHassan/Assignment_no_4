import math

# Ask the user to input the lengths of AB and AC
ab = float(input("Enter the length of AB: "))
ac = float(input("Enter the length of AC: "))

# Calculate the hypotenuse using the Pythagorean Theorem
bc = math.sqrt(ab**2 + ac**2)

# Display the result
print(f"The length of BC (the hypotenuse) is: {bc}")
