from items import *
from text_effect import type_effect

inventory = {}
in_combat = False
equiped_gear = {
    "Helm": None,
    "Body Armor": None,
    "Footwear": None,
    "Weapon": None,
    "Potion": None
}


# Equip, add, and remove messages for items
def equip_message(item):
    type_effect(f"You have equipped {item}!")
    print()


def add_message(item):
    type_effect(f"You have attained {item}!")
    print()


def remove_message(item):
    type_effect(f"You have thrown away {item}...")
    print()


# Simple function to display the inventory
def display_inventory():
    type_effect("Your inventory!")
    print(inventory)
    print()

# Adding items to the inventory


def add_item_to_inventory(item, quantity):
    if item in inventory:
        inventory[item] += quantity
        add_message(item)
    else:
        inventory[item] = quantity
        add_message(item)


# Removing items from the inventory
def remove_item_from_inventory(item, quantity):
    if item in inventory:
        inventory[item] -= quantity
        if inventory[item] <= 0:
            del inventory[item]
        remove_message(item)
    else:
        type_effect("Item not found in inventory.")


def equip(item):
    item_stats = All_items[item]
    if item_stats["type"] == "Weapon":
        equiped_gear["Weapon"] = item
        equip_message(item)

    elif item_stats["type"] == "Helm":
        equiped_gear["Helm"] = item
        equip_message(item)

    elif item_stats["type"] == "Body Armor":
        equiped_gear["Body Armor"] = item
        equip_message(item)

    elif item_stats["type"] == "Footwear":
        equiped_gear["Footwear"] = item
        equip_message(item)

    elif item_stats["type"] == "Potion" and in_combat:
        equiped_gear["Potion"] = item
        equip_message(item)

    elif item_stats["type"] == "Potion" and not in_combat:
        type_effect("You need to be in combat to use a potion!")


def gear():
    type_effect("Your Gear:")
    for gear, item in equiped_gear.items():
        print(f"{gear}: {item}", flush=True)
    print()
