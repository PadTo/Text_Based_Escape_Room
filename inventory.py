inventory = {}


# Simple function to display the inventory
def display_inventory():
    print(inventory)

# Adding items to the inventory


def add_item_to_inventory(item, quantity):
    if item in inventory:
        inventory[item] += quantity
    else:
        inventory[item] = quantity


# Removing items from the inventory
def remove_item_from_inventory(item, quantity):
    if item in inventory:
        inventory[item] -= quantity
        if inventory[item] <= 0:
            del inventory[item]

    else:
        print("Item not found in inventory.")
