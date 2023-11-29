inventory = {}
in_combat = False
equiped_gear = {
    "Helm": None, "\n"
    "Body Armor": None, "\n"
    "Footwear": None, "\n"
    "Weapon": None, "\n"
    "Potion": None
}


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


def equip(item):

    if item["type"] == "Weapon":
        equiped_gear["Weapon"] = item

    elif item["type"] == "Helm":
        equiped_gear["Helm"] = item

    elif item["type"] == "Body Armor":
        equiped_gear["Body Armor"] = item

    elif item["type"] == "Footwear":
        equiped_gear["Footwear"] = item

    elif item["type"] == "Potion" and in_combat:
        equiped_gear["Potion"] = item

    elif item["type"] == "Potion" and not in_combat:
        print("You need to be in combat to use a potion!")


def gear():
    for item_type, item in equiped_gear.items():

        print(f"{item_type}: {item}")

    print()
