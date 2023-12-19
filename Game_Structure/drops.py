
import random
# Ensure All_items is imported correctly
from Game_Structure.items import All_items
from Game_Structure.text_effect import type_effect
from Game_Structure.inventory import add_item_to_inventory, current_space, max_space


def drop_loot(monster, double_loot_chance=False):
    item_tracker = []
    total_items = 0
    initiate_break = False
    if not double_loot_chance:
        multiplier = 1
    else:
        multiplier = 2

    chances = {
        "Common": 70*multiplier,  # 70% chance
        "Uncommon": 50*multiplier,  # 50% chance
        "Rare": 30*multiplier,  # 30% chance
        "Epic": 15*multiplier,  # 15% chance
    }

    item_store = {}

    def get_items_by_rarity(rarity):
        return [item for item, detail in All_items.items() if detail["Rarity"] == rarity]

    def try_drop_item(chance, rarity):
        if random.random() < chance / 100:
            items = get_items_by_rarity(rarity)
            if items:  # Check if list is not empty
                return random.choice(items)
            else:
                return None

    for rarity, chance in chances.items():
        item_drop = try_drop_item(chance, rarity)
        if item_drop:
            if All_items[item_drop]["Type"] in ["Potion", "Health Potion"]:
                quantity = random.randint(1, 3)
                item_store[item_drop] = quantity
                item_tracker.append(item_drop)
            else:
                item_store[item_drop] = 1
                item_tracker.append(item_drop)

    # Specific item drop for Lich King
    if monster["Name"] == "Lich King":
        item_store["Frostmourne"] = 1

    table_len = 85
    table_row = f"{'Item':<25} | {'Quantity':<10} | {'Rarity':<15} | {'Type':<15} | {'Action':<10}"

    type_effect("Drop:")
    print("-" * table_len)
    print(table_row)
    # print(item_tracker)
    n = 0
    for item, quantity in item_store.items():
        total_items += quantity

        print("-" * table_len)
        item_description = f"{item:<25} | {quantity:<10} | {All_items[item]['Rarity']:<15} | {All_items[item]['Type']:<15} | Press: {n}"
        print(item_description)
        n += 1
        pass
    print()

    while True:
        action = input(
            "Choose action: Take All Items (a), Take Single Item (0,1,2,...), Don't Take Loot (e): ").lower()

        if action == 'a':
            if current_space + total_items <= max_space:
                type_effect("You have chosen to take all items:")
                for item, quantity in item_store.items():

                    add_item_to_inventory(item, quantity)
                    initiate_break = True
                    total_items -= 1
            else:
                type_effect("Not enough space for all items.")
                print()

            if initiate_break:
                type_effect("Continuing Journey!")
                print()
                break

            break

        elif action.isdigit():
            index = int(action)
            if 0 <= index < len(item_tracker) and item_tracker[index] != None:
                item = item_tracker[index]
                quantity = item_store[item]
                if current_space + quantity <= max_space:
                    type_effect(f"You have taken {quantity} of {item}.")
                    add_item_to_inventory(item, quantity)
                    item_tracker[index] = None
                    print()
                else:
                    type_effect("Not enough space for this item.")
                    print()
            else:
                type_effect("Invalid item selection.")
                print()

        elif action == 'e':
            type_effect("You have chosen not to take any loot.")
            print()
            break
        else:
            type_effect("Invalid action. Please choose again.")
            print()
