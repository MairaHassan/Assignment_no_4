def main():
    user_list = []

    while True:
        value = input("Enter a value: ")
        if value == "":
            break
        user_list.append(value)

    print("\nHere's the list:", user_list)

if __name__ == "__main__":
    main()
