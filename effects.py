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

                if effect == "Frozen":
                    user_on_going_effects[effect]["Amount"] = False
                    type_effect(
                        "The frost has melted, you can now finally move!")
                    print()
                if effect == "Stunned":
                    user_on_going_effects[effect]["Amount"] = False
                    type_effect("The stun has worn off, attack with rage!")
                    print()

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


def cant_move(type=0):
    # Type 0 is for player, and Type 1 is for monster
    # Text chooses type of text, 0 is for player and 1 is for monster
    type_text = ["You are frozen and can't move..", "You are Stunned and can't move..",
                 "The enemy is frozen and can't move!", "The enemy is stunned and can't move!"]
    n = 1  # This is if there are any other effect added later in the game so that the messages can be easily displayed and added
    if type == 0:
        type_text = type_text[0:n]
        on_going_effects = user_on_going_effects
    else:
        type_text = type_text[n + 1:len(type_text)]
        on_going_effects = monster_on_going_effects

    for effect, details in on_going_effects.items():
        if effect == "Frozen":
            if details["Duration"] > 0:
                type_effect(type_text[0])
                print()
                return True

        if effect == "Stunned":
            if details["Duration"] > 0:
                type_effect(type_text[1])
                print()
                return True

    return False  # Return False if no relevant effect is found
