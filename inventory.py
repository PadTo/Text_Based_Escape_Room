from items import *
from text_effect import type_effect

inventory = {}
max_space = 16
current_space = 0
in_combat = False
equiped_gear = {
    "Helm": None,
    "Body Armor": None,
    "Footwear": None,
    "Weapon": None,
}
character_stats = {
    "Health": 10,
    "Attack": 5,
    "Speed": 5,
    "Dodge": 0
}


# Equip, add, potion drink, and remove messages for items
def equip_message(item):
    type_effect(f"You have equipped {item}!")
    print()


def unequip_message(item):
    type_effect(f"You have unequipped {item}.")
    print()


def add_message(item):
    type_effect(f"You have attained {item}!")
    print()


def remove_message(item):
    type_effect(f"You have thrown away {item}...")
    print()


def potion_drink_message(item):
    type_effect(f"You have drank the {item}!")
    print()


# Function for checking if an item is in the inventory
def is_in_inventory(item):

    for item_inv, quantity in inventory.items():
        if item == item_inv:
            return True

    return False


# Simple function to display the inventory
def display_inventory():
    type_effect("Your inventory!")
    print(inventory)
    print()

# Adding items to the inventory


def add_item_to_inventory(item, quantity):
    global current_space

    if item in inventory:
        inventory[item] += quantity
        current_space += quantity
        add_message(item)
    else:
        inventory[item] = quantity
        current_space += quantity
        add_message(item)


# Removing items from the inventory
def remove_item_from_inventory(item, quantity):
    global current_space

    if item in inventory:
        inventory[item] -= quantity
        current_space -= quantity
        if inventory[item] <= 0:
            del inventory[item]
        remove_message(item)
    else:
        type_effect("Item not found in inventory.")


def use_potion(item):
    if item in inventory and inventory[item] > 0:
        item_stats = All_items[item]

        if item_stats["Type"] == "Health Potion":
            health_boost = item_stats["Health Boost"]
            character_stats["Health"] += health_boost
            inventory[item] -= 1  # Consume one potion

            potion_drink_message(
                f"{item}, health increased by {health_boost}")

    else:
        type_effect("You don't have this potion or it's out of stock.")
        print()


# Function to equip items


def equip(item):

    if is_in_inventory(item):
        item_stats = All_items[item]

        if item_stats["Type"] == "Weapon":
            equiped_gear["Weapon"] = item
            stat_increase(item)
            equip_message(item)

        elif item_stats["Type"] == "Helm":
            equiped_gear["Helm"] = item
            stat_increase(item)
            equip_message(item)

        elif item_stats["Type"] == "Body Armor":
            equiped_gear["Body Armor"] = item
            stat_increase(item)
            equip_message(item)

        elif item_stats["Type"] == "Footwear":
            equiped_gear["Footwear"] = item
            stat_increase(item)
            equip_message(item)

    else:
        type_effect("You don't have this item in your inventory.")
        print()


def unequip(item):

    for slot, equiped_item in equiped_gear.items():
        if equiped_item == item:

            equiped_gear[slot] = None
            unequip_message(item)
            stat_decrease(item)
            return

    type_effect("You don't have this item equiped.")
    print()


# Show character stats:
def character_stats_display():

    type_effect("Your Character Stats:")
    for attribute, stat in character_stats.items():
        type_effect(f"{attribute}: {stat}")
    print()
    pass

# Show item stats:


def item_stats(item):
    type_effect(f"{item} Attributes:")
    item_dic = All_items[item]
    for name, stat in item_dic.items():
        type_effect(f"{name}: {stat}", 0.025)
    print()

# Stat increase function


def stat_increase(item):
    item_attributes = All_items[item]

    # Increase Attack if "Attack Damage" is an attribute of the item
    if "Attack Damage" in item_attributes:
        character_stats["Attack"] += item_attributes["Attack Damage"]

    # Example: Increase Defence if "Defence" is an attribute of the item
    if "Defence" in item_attributes:
        character_stats["Defence"] += item_attributes["Defence"]

# Stat decrease function


def stat_decrease(item):
    item_attributes = All_items[item]

    # Increase Attack if "Attack Damage" is an attribute of the item
    if "Attack Damage" in item_attributes:
        character_stats["Attack"] -= item_attributes["Attack Damage"]

    # Example: Increase Defence if "Defence" is an attribute of the item
    if "Defence" in item_attributes:
        character_stats["Defence"] -= item_attributes["Defence"]


# Show equiped gear
def gear():
    type_effect("Your Gear:")
    for gear, item in equiped_gear.items():
        type_effect(f"{gear}: {item}")
    print()

# Show inventory space


def inventory_space():
    type_effect(f"Current Inventory Space: {current_space}/{max_space}")
    print()
