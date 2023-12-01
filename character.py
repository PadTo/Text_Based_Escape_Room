from text_effect import type_effect

equiped_gear = {
    "Helm": None,
    "Body Armor": None,
    "Footwear": None,
    "Weapon": None,
    "Misc": None,
}

character_stats = {
    "Health": 100,
    "Attack": 10,
    "Defence": 2,
    "Dodge": 2,
    "Name": "Kiausinis"
}

# Show equiped gear


def gear():
    type_effect("Your Gear:")
    for gear, item in equiped_gear.items():
        type_effect(f"{gear}: {item}")
    print()
