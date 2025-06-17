# Set the maximum allowed length
MAX_LENGTH = 3

def shorten(lst):
    # Remove and print elements from the end until the list is MAX_LENGTH long
    while len(lst) > MAX_LENGTH:
        removed_item = lst.pop()
        print("Removed:", removed_item)

def main():
    num_elements = int(input("How many elements do you want to add to the list? "))

    # Get user input to build the list
    user_list = []
    for i in range(num_elements):
        item = input(f"Enter element {i + 1}: ")
        user_list.append(item)

    print("\nOriginal list:", user_list)

    # Call shorten function
    shorten(user_list)

    print("Final list:", user_list)

if __name__ == "__main__":
    main()
