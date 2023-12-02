from inventory import *
from stats import *

stat_increase_char = []
stat_decrease_char = []

# Initial structure of effects dictionaries
user_on_going_effects = {
    "Extra Attack": {"Amount": False, "Duration": 0, "Item": {}},
    "Frozen": {"Amount": False, "Duration": 0, "Item": {}},
    "Stunned": {"Amount": False, "Duration": 0, "Item": {}},

}

monster_on_going_effects = {
    "Extra Attack": {"Amount": False, "Duration": 0, "Item": {}},
    "Frozen": {"Amount": False, "Duration": 0, "Item": {}},
    "Stunned": {"Amount": False, "Duration": 0, "Item": {}},
    "Double Loot Boost": {"Amount": False, "Duration": 0, "Item": {}},

}

non_removable_effects = {"Frozen", "Stunned",
                         "Double Loot Boost", "Extra Attack"}


def user_effects_timer():
    for effect, details in user_on_going_effects.items():
        if details["Duration"] > 0:
            user_on_going_effects[effect]["Duration"] -= 1
            if details["Duration"] <= 0 and effect not in non_removable_effects:

                if "Multiplier" in All_items[details["Item"]]:
                    stat_decrease(
                        None, All_items[details["Item"]]["Multiplier"], 1)
                else:
                    stat_decrease(details["Item"])


def monster_effects_timer():
    for effect, details in monster_on_going_effects.items():
        if details["Duration"] > 0:
            monster_on_going_effects[effect]["Duration"] -= 1
            if details["Duration"] <= 0 and effect not in non_removable_effects:
                stat_decrease(details["Item"])


def reset_effects():
    global user_on_going_effects
    global monster_on_going_effects

    # Reset to the new structure
    user_on_going_effects = {
        "Extra Attack": {"Amount": False, "Duration": 0, "Item": {}},
        "Frozen": {"Amount": False, "Duration": 0, "Item": {}},
        "Stunned": {"Amount": False, "Duration": 0, "Item": {}},
        # Add other effects as needed
    }

    monster_on_going_effects = {
        "Extra Attack": {"Amount": False, "Duration": 0, "Item": {}},
        "Frozen": {"Amount": False, "Duration": 0, "Item": {}},
        "Stunned": {"Amount": False, "Duration": 0, "Item": {}},
        "Double Loot Boost": {"Amount": False, "Duration": 0, "Item": {}},
        # Add other effects as needed
    }
