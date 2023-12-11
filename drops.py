
import random
from items import All_items  # Ensure All_items is imported correctly
from text_effect import type_effect
from inventory import add_item_to_inventory


def drop_loot(monster, double_loot_chance=False):
    item_tracker = []
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
    if monster == "Lich King":
        item_store["Frostmourne"] = 1

    table_len = 80
    table_row = f"{'Item':<25} | {'Quantity':<10} | {'Rarity':<15} | {'Type':<10} | {'Action':<10}"

    type_effect("Drop:")
    print("-" * table_len)
    print(table_row)
    print(item_tracker)
    n = 0
    for item, quantity in item_store.items():

        print("-" * table_len)
        item_description = f"{item:<25} | {quantity:<10} | {All_items[item]['Rarity']:<15} | {All_items[item]['Type']:<10} | Press {n}"
        print(item_description)
        n += 1
        pass
    print()

    action = input(
        "Choose action: Take All Items (a), Take Single Item (0,1,2,...), Don't Take Loot (e): ").lower()

    while True:

        if action == "a":
            type_effect("You chose to take all items.")
            print()
            for item, quantity in item_store.items():

                add_item_to_inventory(item, quantity)

            break

        elif action.isdigit():
            # Take a single item
            index = int(action)
            if 0 <= index < len(item_tracker):
                item = item_tracker[index]
                quantity = item_store[item]
                add_item_to_inventory(item, quantity)
                type_effect(f"You have taken {quantity} of {item}.")

        elif action == "e":
            type_effect("You have chosen not to take any loot.")
            print()
            break

        else:
            type_effect("Invalid action selected.")


    # return item_store
print(drop_loot(monster="none", double_loot_chance=False))
