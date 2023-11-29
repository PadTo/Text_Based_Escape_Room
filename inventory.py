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
character_base_stats = {
    "Health": "10/10",
    "Attack": "5",
    "Speed": "5",
    "Dodge": "0%",
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


# Function for checking if an item is in the inventory
def is_in_inventory(item):
    global is_in
    is_in = False
    for item_inv, quantity in inventory:
        if item == item_inv:
            is_in = True


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

# Function to equip items


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


def character_stats():

    type_effect("Your Character Stats:")
    for attribute, stat in character_base_stats.items():
        type_effect(f"{attribute}: {stat}")
    print()
    pass


def item_stats(item):
    type_effect(f"{item} Attributes:")
    item_dic = All_items[item]
    for name, stat in item_dic.items():
        type_effect(f"{name}: {stat}", 0.025)
    print()


def gear():
    type_effect("Your Gear:")
    for gear, item in equiped_gear.items():
        type_effect(f"{gear}: {item}")
    print()
