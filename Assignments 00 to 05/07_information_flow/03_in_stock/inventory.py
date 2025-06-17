# inventory.py

# Dictionary representing Sophia's fruit inventory
inventory = {
    "apple": 500,
    "banana": 300,
    "pear": 1000,
    "orange": 200,
    "grape": 150
}

def num_in_stock(fruit):
    return inventory.get(fruit.lower(), 0)
