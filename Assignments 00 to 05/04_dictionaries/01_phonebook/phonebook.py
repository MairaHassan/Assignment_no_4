def main():
    phonebook = {}

    while True:
        print("\nPhonebook Menu:")
        print("1. Add contact")
        print("2. Look up contact")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            name = input("Enter name: ")
            number = input("Enter phone number: ")
            phonebook[name] = number
            print(f"Saved {name} with number {number}.")

        elif choice == "2":
            name = input("Enter name to look up: ")
            if name in phonebook:
                print(f"{name}'s number is {phonebook[name]}.")
            else:
                print(f"No contact found for {name}.")

        elif choice == "3":
            print("Exiting phonebook. Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
