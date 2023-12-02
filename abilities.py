import random
from effects import monster_on_going_effects, user_on_going_effects
from items import *
from inventory import *
from stats import *

spell_names = ["Breathing Fire",
               "Collosal Throw",
               "Rejuvination",
               "Curse of the Dead"]


spells_random = {
    spell_names[0]: {
        "Damage": 40,

    },
    spell_names[1]: {
        "Damage": 15,

    },
    spell_names[2]: {

        "Health": 50
    },
    spell_names[3]: {

        "Self Damage": -10,

    }
}


def random_chance(chance):
    probability = random.random()
    if chance/100 > probability:
        return True
    else:
        return False

# Frostmourne


def freeze_ability(target, weapon):
    weapon_trigger_chance = All_items[weapon]["Trigger Chance"]
    if random_chance(weapon_trigger_chance):
        monster_on_going_effects["Frozen"]["Duration"] = 2
        monster_on_going_effects["Frozen"]["Amount"] = True

# Ashbringer


def double_damage_ability(target, weapon):
    weapon_trigger_chance = All_items[weapon]["Trigger Chance"]
    if random_chance(weapon_trigger_chance):
        user_on_going_effects
        weapon_stats = All_items[weapon]
        duration = weapon_stats["Duration"]
        effect_name = weapon_stats["Ability Name"]
        if effect_name in user_on_going_effects:
            user_on_going_effects[effect_name]["Duration"] += duration
        else:
            user_on_going_effects[effect_name] = {
                "Amount": weapon_stats["Multiplier"], "Duration": weapon_stats["Duration"], "Item": weapon}

        stat_increase(None, weapon_stats["Multiplier"], 1)

# Skeleton Shield


def reflect_damage_ability(target, damage, weapon):
    pass


def silence_ability(target, weapon):
    pass


def cast_random_spell_ability(target, weapon):
    weapon_trigger_chance = All_items[weapon]["Trigger Chance"]

    if random_chance(weapon_trigger_chance):
        chosen_spell_name = random.choice(spell_names)
        chosen_spell = spells_random[chosen_spell_name]

        type_effect(f"You have triggered the spell of {chosen_spell_name}")
        for Spell_effects, amount in chosen_spell.items():
            if Spell_effects == "Damage":
                target["Health"] -= amount
                type_effect(
                    f"You have dealt {amount} of damage to the {target['Name']}. Remaining {target['Name']} health: {target['Health']}")

            elif Spell_effects == "Self Damage":
                character_stats["Health"] -= amount
                type_effect(
                    f"You have inflicted {amount} damage to yourself. Current Health: {character_stats['Health']}")

            elif Spell_effects == "Health":
                character_stats[Spell_effects] += amount
                stat_increase_ability(Spell_effects, amount)


# Thunder Hammer


def thunder_strike_ability(user, target_effects, weapon):
    weapon_trigger_chance = All_items[weapon]["Trigger Chance"]
    if random_chance(weapon_trigger_chance):
        target_effects["Thunder Strike"]["Duration"] = 1
        target_effects["Thunder Strike"]["Amount"] = True


def extra_attack_ability(user, user_effects, weapon):
    # This ability might be based on turn count rather than chance
    pass


def make_enemy_slip_ability(user, target, game_state):
    pass


def distract_enemy_ability(user, target, game_state):
    pass


def entangle_enemy_ability(user, target, game_state):
    pass


def return_strike_ability(user, target, game_state):
    # Assuming 'Magic Yo-Yo' weapon
    pass


def trap_enemy_ability(user, target, game_state):
    pass


def squeak_noise_ability(user, target, game_state):
    # Assuming 'Squeaky Hammer' weapon - more for fun, may not need a combat effect
    pass


def rapid_fire_ability(user, target, game_state):
    # Assuming 'AK-47' weapon
    pass


def soft_block_ability(user, target, game_state):
    # Assuming 'Pillow' weapon
    pass


def knowledge_strike_ability(user, target, game_state):
    # Assuming 'Book' weapon
    # Logic for revealing clues or spells
    pass


def stealth_mode_ability(user, target, game_state):
    # Assuming a deliberate action, not a chance-based trigger
    # user.status_effects['stealth_mode'] = 2  # User becomes invisible for 2 turns
    pass


def increase_dodge_chance_potion_ability(potion, user, target, game_state="Combat"):
    if game_state == "Combat" and potion == "Potion of Dodge Chance":
        used_potion = All_items[potion]

        effect_name = "Dodge Boost (Potion)"
        duration = used_potion["Duration"]
        boost_value = used_potion["Dodge"]

        if effect_name in user_on_going_effects:
            user_on_going_effects[effect_name]["Duration"] += duration
        else:
            user_on_going_effects[effect_name] = {
                "Amount": boost_value, "Duration": duration, "Item": potion}

        stat_increase(potion)


def temporary_defence_boost_potion_ability(potion, user, target, game_state="Combat"):
    if game_state == "Combat" and potion == "Potion of Defence":
        used_potion = All_items[potion]

        effect_name = "Defence Boost (Potion)"
        duration = used_potion["Duration"]
        boost_value = used_potion["Defence"]

        if effect_name in user_on_going_effects:
            user_on_going_effects[effect_name]["Duration"] += duration
        else:
            user_on_going_effects[effect_name] = {
                "Amount": boost_value, "Duration": duration, "Item": potion}

        stat_increase(potion)


def greed_effect_potion_ability(potion, user, target, game_state="Combat"):
    if game_state == "Combat" and potion == "Potion of Greed":
        used_potion = All_items[potion]

        effect_name = "Greed Effect (Potion)"
        duration = used_potion["Duration"]
        defence_penalty = used_potion["Defence"]

        if effect_name in user_on_going_effects:
            user_on_going_effects[effect_name]["Duration"] += duration
        else:
            user_on_going_effects[effect_name] = {
                "Amount": defence_penalty, "Duration": duration, "Item": potion}

        stat_decrease(potion)


def random_effect_potion_ability(potion, user, target, game_state="Combat"):
    if game_state == "Combat" and potion == "Potion of the Unknown":
        possible_potions = ["Potion of Vulnerability", "Potion of Fortitude",
                            "Potion of Agility", "Potion of Clumsiness"]
        chosen_potion = random.choice(possible_potions)
        print(chosen_potion)
        chosen_potion_stats = All_items[chosen_potion]
        effect_name = chosen_potion
        duration = chosen_potion_stats["Duration"]

        amount = chosen_potion_stats.get(
            "Defence", 0) or chosen_potion_stats.get("Dodge", 0)
        print(amount)

        if effect_name in user_on_going_effects:
            user_on_going_effects[effect_name]["Duration"] += duration
        else:
            user_on_going_effects[effect_name] = {
                "Amount": amount, "Duration": duration, "Item": chosen_potion}

        if amount > 0:
            stat_increase(chosen_potion)
        else:
            # Assuming the negative amount indicates a decrease
            stat_decrease(chosen_potion)


item_abilities = {
    "Frostmourne": freeze_ability,
    "Ashbringer": double_damage_ability,
    "Skeleton Shield": reflect_damage_ability,
    "Crossbow of Silence": silence_ability,
    "Mystic Wand": cast_random_spell_ability,
    "Thunder Hammer": thunder_strike_ability,
    "Dual Daggers": extra_attack_ability,
    "Banana Peel": make_enemy_slip_ability,
    "Rubber Chicken": distract_enemy_ability,
    "Spaghetti Whip": entangle_enemy_ability,
    "Magic Yo-Yo": return_strike_ability,
    "Bubble Blower": trap_enemy_ability,
    "Squeaky Hammer": squeak_noise_ability,
    "AK-47": rapid_fire_ability,
    "Pillow": soft_block_ability,
    "Book": knowledge_strike_ability,
    "Blanket": stealth_mode_ability,
    "Potion of Dodge Chance": increase_dodge_chance_potion_ability,
    "Potion of Defence": temporary_defence_boost_potion_ability,
    "Potion of Greed": greed_effect_potion_ability,
    "Potion of the Unknown": random_effect_potion_ability,
    # "Potion of Fortitude":
    # "Potion of Vulnerability":
    # "Potion of Agility":
    # "Potion of Clumsiness":

}


def trigger_weapon_ability(target):
    equipped_weapon_name = equiped_gear.get("Weapon")
    if equipped_weapon_name is not None:

        item_trigger_ability = item_abilities[equipped_weapon_name]

        if item_trigger_ability is not None and "Special Trigger" in All_items[equipped_weapon_name]:
            item_trigger_ability(target, equipped_weapon_name)


def trigger_shield_ability(target):
    equipped_items = get_equipped_items()
    if equipped_items["Name"] == "Shield":
        weapon = equipped_items["Shield"]
        item_trigger_ability = item_abilities[equipped_items]
        item_trigger_ability(weapon, target)
