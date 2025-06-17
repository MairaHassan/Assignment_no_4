# fruit_store.py

from inventory import num_in_stock

def main():
    fruit = input("Enter a fruit: ").strip().lower()
    count = num_in_stock(fruit)

    if count > 0:
        print("\nThis fruit is in stock! Here is how many:\n")
        print(count)
    else:
        print("\nThis fruit is not in stock.")

if __name__ == "__main__":
    main()
