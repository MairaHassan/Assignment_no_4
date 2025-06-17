def get_first_element(lst):
    # Print the first element of the list
    print("First element:", lst[0])

def main():
    num_elements = int(input("How many elements do you want to add to the list? "))

    # Initialize empty list
    user_list = []

    # Collect elements from the user
    for i in range(num_elements):
        element = input(f"Enter element {i + 1}: ")
        user_list.append(element)

    print("\nComplete list:", user_list)

    # Call the function to print the first element
    get_first_element(user_list)

if __name__ == "__main__":
    main()
