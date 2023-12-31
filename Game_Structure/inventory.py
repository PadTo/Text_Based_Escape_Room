from Game_Structure.items import *
from Game_Structure.text_effect import type_effect
from Game_Structure.display_effect import *
from Game_Structure.character import *
from Game_Structure.abilities import *
from Game_Structure.stats import stat_increase, stat_decrease

inventory = {}      # Empty inventory
max_space = 16      # Maximum Space
current_space = 0   # Constant for current inventory space
inventory_item_tracker = []
# Equip, add, potion drink, and remove messages for items


def equip_message(item):
    type_effect(f"You have equipped {item}!")


def unequip_message(item):
    type_effect(f"You have unequipped {item}.")


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


# Adding items to the inventory


def add_item_to_inventory(item, quantity):
    global current_space

    if item not in inventory and item not in inventory_item_tracker:
        inventory_item_tracker.append(item)

    if current_space + quantity > max_space:
        type_effect("Not enough space in inventory.")
        return

    # Check if the item is already in the inventory
    if item in inventory:
        inventory[item] += quantity
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
            inventory_item_tracker.remove(item)
            del inventory[item]
        remove_message(item)
    else:
        type_effect("Item not found in inventory.")
        print()


def use_potion_out_of_combat(item):
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
                inventory_item_tracker.remove(item)
                del inventory[item]

        elif item_stats["Type"] == "Potion":
            type_effect("You have to be in combat to use this potion.")
            print()

    else:
        type_effect("You don't have this potion or it's out of stock.")
        print()


# Function to equip items


def equip(item):

    if is_in_inventory(item):
        item_stats = All_items[item]

        if item_stats["Type"] == "Weapon" and item_stats["Weapon Type"] != "Shield":
            if equiped_gear["Weapon"] != None:
                unequip_message(equiped_gear["Weapon"])
            stat_decrease(equiped_gear["Weapon"])
            print()
            equiped_gear["Weapon"] = item
            equip_message(item)
            stat_increase(item)
            print()

        elif item_stats["Type"] == "Helm":
            if equiped_gear["Helm"] != None:
                unequip_message(equiped_gear["Helm"])

            stat_decrease(equiped_gear["Helm"])
            print()
            equiped_gear["Helm"] = item
            stat_increase(item)
            equip_message(item)
            print()

        elif item_stats["Type"] == "Body Armor":
            if equiped_gear["Body Armour"] != None:
                unequip_message(equiped_gear["Body Armour"])

            stat_decrease(equiped_gear["Body Armor"])
            print()
            equiped_gear["Body Armor"] = item
            equip_message(item)
            stat_increase(item)
            print()

        elif item_stats["Type"] == "Footwear":
            if equiped_gear["Footwear"] != None:
                unequip_message(equiped_gear["Footwear"])

            stat_decrease(equiped_gear["Footwear"])
            print()
            equiped_gear["Footwear"] = item
            stat_increase(item)
            equip_message(item)
            print()

        elif item_stats["Type"] == "Weapon" and item_stats["Weapon Type"] == "Shield":
            if equiped_gear["Shield"] != None:
                unequip_message(equiped_gear["Shield"])

            stat_decrease(equiped_gear["Shield"])
            print()
            equiped_gear["Shield"] = item
            stat_increase(item)
            equip_message(item)
            print()

        elif item_stats["Type"] == "Misc":
            if equiped_gear["Misc"] != None:
                unequip_message(equiped_gear["Misc"])

            stat_decrease(equiped_gear["Misc"])
            print()
            equiped_gear["Misc"] = item
            stat_increase(item)
            equip_message(item)
            print()
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


# Show inventory space

def inventory_space():
    if current_space == 0:
        type_effect(f"Your inventory is empty...")

    else:
        type_effect(f"Current Inventory Space: {current_space}/{max_space}")
        print()


def display_inventory():
    i = 0
    type_effect("Your Inventory:")
    table_len = 70
    print("-" * table_len)
    print(f"{'Item':<25} | {'Quantity':<10} | {'Type':<15} | {'Use/Equip':<10}")
    print("-" * table_len)
    for item, quantity in inventory.items():
        current_item = All_items[item]
        if "Weapon Type" in current_item:
            print(
                f"{item:<25} | {quantity:<10} | {current_item['Weapon Type']:<15} | Press: {i}")
        else:
            print(
                f"{item:<25} | {quantity:<10} | {current_item['Type']:<15} | Press: {i}")
        i += 1
    print("-" * table_len)
    print()

    while True:
        try:
            inventory_index = int(input(
                "Enter a key to take an action: "))
            if inventory_index < len(inventory_item_tracker):
                chosen_item = inventory_item_tracker[inventory_index]
                if All_items[chosen_item]["Type"] == "Health Potion" or All_items[chosen_item]["Type"] == "Potion":
                    use_potion_out_of_combat(chosen_item)
                else:
                    equip(chosen_item)

            else:
                type_effect(
                    "Invalid input. If you want to exit the inventory press any key (except numbers).")
                print()
        except ValueError:
            type_effect("Exiting inventory.")
            print()
            return False


def use_potion_in_combat(potion_name, game_state="Combat", user="Self", target="Enemy"):
    global current_space

    from Game_Structure.abilities import item_abilities

    if All_items[potion_name]["Type"] == "Health Potion":
        type_effect(f"You used {potion_name}.")
        stat_increase(potion_name)

    if potion_name in item_abilities:
        type_effect(f"You used {potion_name}.")
        print(item_abilities[potion_name])
        item_abilities[potion_name](potion_name, user, target, game_state)

    inventory[potion_name] -= 1
    current_space -= 1
    if inventory[potion_name] <= 0:
        del inventory[potion_name]

# Check for potions in inventory:


def check_if_potions_true(game_state="Combat"):
    i = 0  # To count the items position in the table
    store_potion_names = []
    has_potions = False
    for item, quantity in inventory.items():
        item_type = All_items[item]["Type"]
        if "Potion" in item_type or "Health Potion" in item_type:
            display_effects(item, i, quantity, 0)
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
                use_potion_in_combat(
                    store_potion_names[potion_index], game_state)
                return True
            else:
                type_effect(
                    "Invalid input. If you want to take another action press any key (except numbers).")
                print()
        except ValueError:
            type_effect("Exiting potion inventory.")
            print()
            return False


def check_if_weapons_or_shields_true(type=0):
    # Type 0 for weapons, type 1 for shields

    item_type = ["Weapon", "Shield"]

    i = 0  # To count the items position in the table
    store_weapon_names = []
    has_weapons = False
    for item, quantity in inventory.items():
        inventory_item_type = All_items[item]["Type"]
        if item_type[type] in inventory_item_type:
            display_effects(item, i, quantity, 1)
            i += 1
            has_weapons = True
            store_weapon_names.append(item)

    if not has_weapons:
        type_effect(
            f"You don't have any {item_type[type]}'s , choose another action")
        print()
        return False

    while True:
        try:
            weapon_index = int(input(
                "Select a weapon to equip (enter the number): "))
            if weapon_index < len(store_weapon_names):
                equip(store_weapon_names[weapon_index])
                return True
            else:
                type_effect(
                    "Invalid input. If you want to take another action press any key (except numbers).")
                print()
        except ValueError:
            type_effect("Exiting weapon inventory.")
            print()
            return False


def check_if_equiped_item_abilities_true():
    i = 0  # To count the items position in the table

    store_weapon_abilities = []
    store_weapons = []
    has_abilities = False
    for slot, item in equiped_gear.items():

        if item in All_items:

            item_stats = All_items[item]
            if "Special Cast" in item_stats:

                display_effects(item, i, 0, 2)
                i += 1
                has_abilities = True
                store_weapons.append(item)
                store_weapon_abilities.append(item_stats["Special Cast"])

    if not has_abilities:
        type_effect(
            "You don't have any abilities to use, choose another action")
        print()
        return False

    while True:
        from Game_Structure.abilities import item_abilities
        try:
            spell_index = int(input(
                "Select a spell to use (enter the number): "))
            if spell_index < len(store_weapons):
                selected_weapon = store_weapons[spell_index]
                ability_function = item_abilities[selected_weapon]
                result = ability_function(None, selected_weapon)

                # Check the result and return accordingly
                if result == False:
                    return False
                elif result == True:
                    return True
                else:
                    return True

            else:
                type_effect(
                    "Invalid input. If you want to take another action press any key (except numbers).")
                print()
        except ValueError:
            type_effect("Exiting weapon inventory.")
            print()
            return False
