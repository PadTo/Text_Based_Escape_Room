from items import *
from text_effect import type_effect
from character import *

inventory = {}      # Empty inventory
max_space = 16      # Maximum Space
current_space = 0   # Constant for current inventory space
in_combat = False

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


def display_inventory():
    type_effect("Your Inventory:")
    table_len = 60
    print("-" * table_len)
    print(f"{'Item':<25} | {'Quantity':<10} | {'Type':<10}")
    print("-" * table_len)
    for item, quantity in inventory.items():
        current_item = All_items[item]
        print(f"{item:<25} | {quantity:<10} | {current_item['Type']:<10}")
    print("-" * table_len)
    print()


# Adding items to the inventory


def add_item_to_inventory(item, quantity):
    global current_space

    if current_space + quantity > max_space:
        type_effect("Not enough space in inventory.")
        return

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
        print()


def use_potion(item):
    global current_space
    if item in inventory and inventory[item] > 0:
        item_stats = All_items[item]

        if item_stats["Type"] == "Health Potion":
            health_boost = item_stats["Health Boost"]
            character_stats["Health"] += health_boost
            inventory[item] -= 1  # Consume one potion
            current_space -= 1

            potion_drink_message(
                f"{item}, health increased by {health_boost}")
            if inventory[item] <= 0:
                del inventory[item]

        elif item_stats["Type"] == "Potion" and not in_combat:
            type_effect("You have to be in combat to use this potion.")
            print()
        elif item_stats["Type"] == "Potion" and in_combat:
            pass
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
    if current_space == 0:
        type_effect(f"Your inventory is empty...")

    else:
        type_effect(f"Current Inventory Space: {current_space}/{max_space}")
        print()


def display_effect(item, quantity, number):
    table_len = 85
    if number == 0:
        type_effect("Your Can Use:", 0.04)
        print("-" * table_len)
        print(
            f"{'Item':<25} | {'Quantity':<10} | {'Type':<15} | {'Use':<10} | {'Duration':<10}")
        print("-" * table_len)
        current_item = All_items[item]
        print(
            f"{item:<25} | {quantity:<10} | {current_item['Type']:<15} | Press: {number:<3} | {current_item['Duration']} Rounds")
        print("-" * table_len)
    else:
        current_item = All_items[item]
        print(
            f"{item:<25} | {quantity:<10} | {current_item['Type']:<15} | Press: {number:<3} | {current_item['Duration']} Rounds")
        print("-" * table_len)


# Check for potions in inventory:


def check_if_potions_true():
    i = 0  # To count the items position in the table
    store_potion_names = []
    for item, quantity in inventory.items():
        if item == "Potion" or "Health Potion":
            display_effect(item, quantity, i)
            i += 1
            has_potions = True
            store_potion_names.append(item)

    if not has_potions:
        type_effect("You don't have any potions, choose another action")
        print()
        return False
    while True:
        try:
            potion_index = int(input(
                "Select a potion to use (enter the number): "))
            if potion_index < len(store_potion_names):
                use_potion(store_potion_names[potion_index])
                return True
            else:
                type_effect(
                    "Invalid input. If you want to take another action press any key (except numbers).")
                print()
        except ValueError:
            type_effect("Exiting potion inventory.")
            print()
            return False

# use_potion function


def use_potion(potion_name):
    type_effect(f"You used {potion_name}.")
    inventory[potion_name] -= 1
    if inventory[potion_name] <= 0:
        del inventory[potion_name]


def check_equiped_item_abilities():
    pass


add_item_to_inventory("Potion of Small Health", 3)
add_item_to_inventory("Potion of Dodge Chance", 2)
check_if_potions_true()
