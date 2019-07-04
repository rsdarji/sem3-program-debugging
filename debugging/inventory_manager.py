def enter_items():
    items = []
    while True:
        name = input("Enter an item name: ").title()
        qty = input("Enter the item quantity: ")
        items.append((name, qty))

        command = input("Continue? [y/n]: ").lower()
        while command not in ('y', 'n'):
            command = input("Invalid command...\nContinue? [y/n]: ").lower()

        if command == 'n':
            break

    return items

def sort_inventory(inventory):
    command = input("Do you want to sort the inventory by quantity or name? [qty/name]: ").lower()
    while command not in ('qty', 'name'):
        command = input("Invalid command...\nSort the inventory by quantity or name? [qty/name]: ").lower()

    if command == 'name':
        inventory.sort()
    elif command == 'qty':
        inventory.sort(key=lambda x: x[::-1])

    return inventory
if __name__ == '__main__':
    # Get inventory from user
    inventory = enter_items()

    # Prompt the user for a way to sort the inventory
    inventory = sort_inventory(inventory)

    print("Thank you! You inventory will be stored in the file 'inventory.txt'.")
    with open('inventory.txt', 'w') as f:
        for name, qty in inventory:
            f.write("{}: {}\n".format(name, qty))




