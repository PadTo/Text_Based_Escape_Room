from text_effect import type_effect

equiped_gear = {
    "Helm": None,
    "Body Armor": None,
    "Footwear": None,
    "Weapon": None,
    "Misc": None,
    "Shield": None
}

character_stats = {
    "Health": 100,
    "Attack": 10,
    "Defence": 2,
    "Dodge": 2,
    "Name": "Kiausinis"
}


def character_stats_before_combat(character_stats):
    stats_before_combat = character_stats
    return stats_before_combat


def health_after_combat():
    health = character_stats["Health"]
    return health
# Show equiped gear


def gear():
    type_effect("Your Gear:")
    for gear, item in equiped_gear.items():
        type_effect(f"{gear}: {item}")
    print()


def get_equipped_items():
    equipped_items = []
    if equiped_gear["Weapon"]:
        equipped_items.append(equiped_gear["Weapon"])
    if equiped_gear["Shield"]:
        equipped_items.append(equiped_gear["Shield"])
    return equipped_items
