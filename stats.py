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
