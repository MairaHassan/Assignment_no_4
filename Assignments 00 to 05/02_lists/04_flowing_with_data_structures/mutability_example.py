def add_three_copies(target_list, data):
    # This function modifies the list directly
    for _ in range(3):
        target_list.append(data)

def main():
    # Get input from the user
    message = input("Enter a message to copy: ")

    # Start with an empty list
    messages = []

    print("\nList before:", messages)

    # Call the helper function that modifies the list
    add_three_copies(messages, message)

    print("List after:", messages)

if __name__ == "__main__":
    main()
