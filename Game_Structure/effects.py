from inventory import *
from stats import *

stat_increase_char = []
stat_decrease_char = []

# Initial structure of effects dictionaries
user_on_going_effects = {
    "Extra Attack": {"Amount": False, "Duration": 0, "Item": {}},
    "Frozen":  {"Amount": False, "Duration": 0, "Item": {}},
    "Stunned": {"Amount": False, "Duration": 0, "Item": {}},
    "Stealth": {"Amount": False, "Duration": 0, "Item": {}},
    "Disarm":  {"Amount": False, "Duration": 0, "Item": {}},

}

monster_on_going_effects = {
    "Extra Attack": {"Amount": False, "Duration": 0, "Item": {}},
    "Frozen": {"Amount": False, "Duration": 0, "Item": {}},
    "Stunned": {"Amount": False, "Duration": 0, "Item": {}},
    "Stealth": {"Amount": False, "Duration": 0, "Item": {}},
    "Double Loot Boost": {"Amount": False, "Duration": 0, "Item": {}},
    "Silence": {"Amount": False, "Duration": 0, "Item": {}},

}


def check_if_silenced():
    if monster_on_going_effects["Silence"]["Duration"] > 0:
        return True
    else:
        return False  # Explicitly return False if not silenced


user_cooldowns = {
    "Trap": {"Cooldown": 0, "Item": {}},
    "Stealth": {"Cooldown": 0, "Item": {}},
    "Silence": {"Cooldown": 0, "Item": {}},
}

monster_cooldowns = {
    "Trap":    {"Cooldown": 0, "Ability": {}},
    "Stealth": {"Cooldown": 0, "Ability": {}},
    "Silence": {"Cooldown": 0, "Ability": {}},
    "Bleed":   {"Cooldown": 0, "Ability": {}},
    "Disarm":  {"Cooldown": 0, "Ability": {}},

}


non_removable_effects = {"Frozen", "Stunned",
                         "Double Loot Boost", "Extra Attack"}

static_effect = ["Frozen", "Stunned", "Slip", "Trap"]


def user_effects_timer():
    for effect, details in user_on_going_effects.items():
        if details["Duration"] > 0:
            user_on_going_effects[effect]["Duration"] -= 1
            if details["Duration"] <= 0:

                if effect == "Frozen" and user_on_going_effects[effect]["Amount"] == True:
                    user_on_going_effects[effect]["Amount"] = False
                    user_on_going_effects[effect]["Item"] = {}
                    type_effect(
                        "The frost has melted, you can now finally move!")
                    print()
                if effect == "Stunned" and user_on_going_effects[effect]["Amount"] == True:
                    user_on_going_effects[effect]["Amount"] = False
                    user_on_going_effects[effect]["Item"] = {}
                    type_effect("The stun has worn off, attack with rage!")
                    print()

                if effect == "Slip" and user_on_going_effects[effect]["Amount"] == True:
                    user_on_going_effects[effect]["Amount"] = False
                    user_on_going_effects[effect]["Item"] = {}
                    type_effect(
                        "The headache has worn off, you can now finally move!")
                    print()
                if effect == "Trap" and user_on_going_effects[effect]["Amount"] == True:
                    user_on_going_effects[effect]["Amount"] = False
                    user_on_going_effects[effect]["Item"] = {}
                    type_effect("The trap has worn off, attack with rage!")
                    print()

                if effect == "Double Damage":
                    stat_decrease(
                        details["Item"], All_items[details["Item"]]["Multiplier"], 1)

                if effect != "Double Damage":
                    if details["Item"] != {} and effect not in static_effect:

                        if All_items[effect]["Amount"] > 0:
                            stat_decrease(details["Item"])

                        elif All_items[effect]["Amount"] < 0:
                            stat_increase(details["Item"])


def monster_effects_timer():
    for effect, details in monster_on_going_effects.items():
        if details["Duration"] > 0:
            monster_on_going_effects[effect]["Duration"] -= 1
            if details["Duration"] <= 0 and effect not in non_removable_effects:

                if effect == "Frozen":
                    monster_on_going_effects[effect]["Amount"] = False
                    type_effect(
                        "The frost has melted, the enemy can now finally move..")
                    print()
                if effect == "Stunned":
                    monster_on_going_effects[effect]["Amount"] = False
                    type_effect(
                        "The stun has worn off, the enemy can now attack with rage!")
                    print()

                if effect == "Slip":
                    monster_on_going_effects[effect]["Amount"] = False
                    type_effect(
                        "The headache has worn off, the enemy can now attack!")
                    print()
                if effect == "Trap":
                    monster_on_going_effects[effect]["Amount"] = False
                    type_effect(
                        "The trap has worn off, the enemy can now attack")
                    print()

                if effect == "Silence":
                    monster_on_going_effects[effect]["Amount"] = False
                    type_effect(
                        "The silence has worn off, the enemy can now cast spells!")
                    print()


def reset_effects():
    global user_on_going_effects
    global monster_on_going_effects

    # Reset to the new structure
    user_on_going_effects = {
        "Extra Attack": {"Amount": False, "Duration": 0, "Item": {}},
        "Frozen": {"Amount": False, "Duration": 0, "Item": {}},
        "Stunned": {"Amount": False, "Duration": 0, "Item": {}},
        "Stealth": {"Amount": False, "Duration": 0, "Item": {}}
        # Add other effects as needed
    }

    monster_on_going_effects = {
        "Extra Attack": {"Amount": False, "Duration": 0, "Item": {}},
        "Frozen": {"Amount": False, "Duration": 0, "Item": {}},
        "Stunned": {"Amount": False, "Duration": 0, "Item": {}},
        "Stealth": {"Amount": False, "Duration": 0, "Item": {}},
        "Double Loot Boost": {"Amount": False, "Duration": 0, "Item": {}},
        # Add other effects as needed
    }


def cant_move(type=0):
    # Messages for player and monster effects
    effect_messages = {
        "Frozen": ["You are frozen and can't move..", "The enemy is frozen and can't move!"],
        "Stunned": ["You are stunned and can't move..", "The enemy is stunned and can't move!"],
        "Slip": ["You have slipped, hit your head and can't move...", "The enemy has slipped, hit its head and can't move..."],
        "Trap": ["You are trapped...", "The enemy is trapped..."]
    }

    # Choose the correct effects dictionary based on type
    on_going_effects = user_on_going_effects if type == 0 else monster_on_going_effects

    # Check each effect
    for effect, details in on_going_effects.items():
        if details["Duration"] > 0 and effect in effect_messages:
            type_effect(effect_messages[effect][type])
            print()
            return True

    return False  # Return False if no relevant effect is found


def cooldowns_effect_timer():
    for effect, details in user_cooldowns.items():
        if details["Cooldown"] > 0:
            details["Cooldown"] -= 1

            if details["Cooldown"] == 0:
                type_effect(f"{details['Item']} is now ready to use again.")
                details["Item"] = {}  # Reset the item key if needed


def monster_cooldowns_effect_timer():
    for effect, details in monster_cooldowns.items():
        if details["Cooldown"] > 0:
            details["Cooldown"] -= 1

            if details["Cooldown"] == 0:
                details["Ability"] = {}  # Reset the item key if needed
