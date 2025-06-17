def main():
    fruit_prices = {
        "apple": 3.5,
        "durian": 15.0,
        "jackfruit": 25.0,
        "kiwi": 4.5,
        "rambutan": 6.5,
        "mango": 10.0
    }

    total_cost = 0.0

    for fruit, price in fruit_prices.items():
        try:
            qty = int(input(f"How many ({fruit}) do you want?: "))
            total_cost += qty * price
        except ValueError:
            print("Please enter a valid number. We'll count that as 0.")

    print(f"\nYour total is ${total_cost}")
    
if __name__ == "__main__":
    main()
