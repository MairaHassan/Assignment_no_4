# Constant representing adult age in the US
ADULT_AGE = 18

def is_adult(age):
    return age >= ADULT_AGE

# Get user input and convert it to an integer
age_input = int(input("How old is this person?: "))

# Call the function and print the result
print(is_adult(age_input))
