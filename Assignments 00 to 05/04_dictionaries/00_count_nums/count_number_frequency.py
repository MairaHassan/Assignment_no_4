def main():
    counts = {}

    while True:
        entry = input("Enter a number: ")
        if entry == "":
            break
        try:
            num = int(entry)
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        except ValueError:
            print("Please enter a valid number.")

    print()  # Blank line before results

    for number, count in counts.items():
        print(f"{number} appears {count} times.")

if __name__ == "__main__":
    main()
