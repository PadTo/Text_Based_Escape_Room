from character import character_stats
from items import All_items
from text_effect import type_effect


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
    if item is None:
        return
    else:
        item_attributes = All_items[item]

        # Increase Attack if "Attack Damage" is an attribute of the item
        if "Attack Damage" in item_attributes:
            character_stats["Attack"] -= item_attributes["Attack Damage"]

        # Example: Increase Defence if "Defence" is an attribute of the item
        if "Defence" in item_attributes:
            character_stats["Defence"] -= item_attributes["Defence"]

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
