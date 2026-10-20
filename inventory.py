inventory = {
    "Laptop": 10,
    "Mouse": 25,
    "Keyboard": 15
}

def show_inventory():
    print("Current Inventory:")
    for product, quantity in inventory.items():
        print(f"{product}: {quantity}")

show_inventory()
