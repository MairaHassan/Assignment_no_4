def get_last_element(lst):
    # Print the last element of the list
    print("Last element:", lst[-1])

def main():
    num_elements = int(input("How many elements do you want to add to the list? "))

    # Initialize an empty list
    user_list = []

    # Collect elements from the user
    for i in range(num_elements):
        element = input(f"Enter element {i + 1}: ")
        user_list.append(element)

    print("\nComplete list:", user_list)

    # Call the function to print the last element
    get_last_element(user_list)

if __name__ == "__main__":
    main()
