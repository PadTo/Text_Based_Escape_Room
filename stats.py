from character import character_stats
from items import All_items
from text_effect import type_effect


def stat_increase_ability(stat, amount):
    if stat == "Attack Damage":
        character_stats["Attack"] += amount
        type_effect(
            f"You have increased your {stat} by {amount}!. New total: {character_stats['Attack']}.")
    if stat == "Defence":
        character_stats["Defence"] += amount
        type_effect(
            f"You have increased your {stat} by {amount}!. New total: {character_stats['Defence']}.")
    if stat == "Dodge":
        character_stats["Dodge"] += amount
        type_effect(
            f"You have increased your {stat} by {amount}!. New total: {character_stats['Dodge']}.")

    if stat == "Health":
        character_stats["Health"] += amount
        type_effect(
            f"You have increased your {stat} by {amount}!. New total: {character_stats['Health']}.")


def stat_increase(item=None, multiplier=0, boost_character_multiplier=0):

    if boost_character_multiplier == 1:
        character_stats["Attack"] = character_stats["Attack"]*multiplier
        type_effect(
            f"Damage multiplier activated ({multiplier}x damage increase). New total: {character_stats['Attack']}.")

    else:
        item_attributes = All_items[item]

        if "Attack Damage" in item_attributes:
            character_stats["Attack"] += item_attributes["Attack Damage"]
            type_effect(
                f"Attack increased by {item_attributes['Attack Damage']}. New total: {character_stats['Attack']}.")

        if "Defence" in item_attributes:
            character_stats["Defence"] += item_attributes["Defence"]
            type_effect(
                f"Defence increased by {item_attributes['Defence']}. New total: {character_stats['Defence']}.")

        if "Dodge" in item_attributes:
            character_stats["Dodge"] += item_attributes["Dodge"]
            type_effect(
                f"Dodge increased by {item_attributes['Dodge']}. New total: {character_stats['Dodge']}.")

        if "Health" in item_attributes or "Health Boost" in item_attributes:
            health_increase = item_attributes.get(
                "Health", 0) + item_attributes.get("Health Boost", 0)
            character_stats["Health"] += health_increase
            type_effect(
                f"Health increased by {health_increase}. New total: {character_stats['Health']}.")


def stat_decrease(item=None, multiplier=0, lower_character_multiplier=0):

    if lower_character_multiplier == 1:  # 1 means that it decreases damage based on the multiplier, 0 skips this line of code
        character_stats["Attack"] = character_stats["Attack"]/multiplier
        type_effect(
            f"Damage multiplier deactivated ({multiplier}x damage decrease). New total: {character_stats['Attack']}.")

    else:
        if item is None:
            return
        else:
            item_attributes = All_items[item]

            if "Attack Damage" in item_attributes:
                character_stats["Attack"] -= item_attributes["Attack Damage"]
                type_effect(
                    f"Attack decreased by {item_attributes['Attack Damage']}. New total: {character_stats['Attack']}.")

            if "Defence" in item_attributes:
                character_stats["Defence"] -= item_attributes["Defence"]
                type_effect(
                    f"Defence decreased by {item_attributes['Defence']}. New total: {character_stats['Defence']}.")

            if "Dodge" in item_attributes:
                character_stats["Dodge"] -= item_attributes["Dodge"]
                type_effect(
                    f"Dodge decreased by {item_attributes['Dodge']}. New total: {character_stats['Dodge']}.")

            if "Health" in item_attributes:
                character_stats["Health"] -= item_attributes["Health"]
                type_effect(
                    f"Health decreased by {item_attributes['Health']}. New total: {character_stats['Health']}.")

# Show character stats


def character_stats_display():
    type_effect("Your Character Stats:")
    for attribute, stat in character_stats.items():
        type_effect(f"{attribute}: {stat}")
    print()

# Show item stats


def item_stats(item):
    type_effect(f"{item} Attributes:")
    item_dic = All_items[item]
    for name, stat in item_dic.items():
        type_effect(f"{name}: {stat}", 0.025)
    print()
