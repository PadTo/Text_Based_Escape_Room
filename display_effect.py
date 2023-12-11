from items import All_items
from text_effect import type_effect


def display_effects(item, number, quantity=0, display_type=0):
    current_item = All_items.get(item, {})
    table_len = [80, 85, 140]
    text = ["You Can Use:", "You Can Equip:", "You Can Cast:"]

    if display_type == 0:  # For Potions
        table_row = f"{'Item':<25} | {'Quantity':<10} | {'Type':<15} | {'Use':<10} | {'Duration':<10}"
        item_description = f"{item:<25} | {quantity:<10} | {current_item.get('Type', 'N/A'):<15} | Press: {number:<3} | {current_item.get('Duration', 'N/A')} Rounds"
    elif display_type == 1:  # For Weapons
        table_row = f"{'Item':<25} | {'Weapon Type':<15} | {'Use':<10}"
        item_description = f"{item:<25} | {current_item.get('Weapon Type', 'N/A'):<15} | Press: {number:<3}"
    elif display_type == 2:  # For Item Spells
        table_row = f"{'Item':<25} | {'Ability':<15} | {'Use':<10} | {'Cooldown':<5} | {'Description':<20}"
        ability_name = current_item["Ability Name"]
        item_description = f"{item:<25} | {ability_name:<15} | Press: {number:<3} | {current_item.get('Cooldown', 'N/A')} Rounds | {current_item.get('Special Cast', 'N/A')}"

    if number == 0:
        type_effect(text[display_type], 0.04)
        print(table_row)
        print("-" * table_len[display_type])

    print(item_description)
    print("-" * table_len[display_type])


def display_drop(item, number, quantity):
    table_len = 80
    table_row = f"{'Item':<25} | {'Weapon Type':<15} | {'Use':<10}"
    item_description = f"{item:<25} | {item.get('Weapon Type', 'N/A'):<15} | Press: {number:<3}"

    if number == 0:
        type_effect("Dropped Items")
        print(table_row)
        print("-" * table_len)

    print(item_description)
    print("-" * table_len)

    pass
