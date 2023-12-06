import random
from effects import monster_on_going_effects, user_on_going_effects
from items import *
from inventory import *
from stats import *
from character import equiped_gear
import math

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
    if target["Name"] == "Lich King":
        type_effect(f"{All_items[weapon]['Ability Name']} Ability Triggered!")
        type_effect(
            f"But did you really think freeze works on the {target['Name']}?!?! ")
    else:
        weapon_trigger_chance = All_items[weapon]["Trigger Chance"]
        if random_chance(weapon_trigger_chance):
            monster_on_going_effects["Frozen"]["Duration"] = All_items[weapon]["Duration"]
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


def reflect_damage_ability(target, weapon, damage=0):
    weapon_trigger_chance = All_items[weapon]["Trigger Chance"]
    if random_chance(weapon_trigger_chance):
        print("Triggering shield special ability")
        damage_returned = math.ceil(
            damage*(All_items[weapon]["Damage Reduction"] / 100))
        type_effect(
            f"{All_items[weapon]['Ability Name']} Activated: {damage_returned} returned!")
        new_damage = damage - damage_returned
        target["Health"] -= damage_returned
        type_effect(
            f"{target['Name']} Health: {target['Health']}")
        print()
        return new_damage
    else:
        return damage

# CrossBow of Silence


def silence_ability(target, weapon):
    weapon_stats = All_items[weapon]
    type_effect(f"The enemy has been silenced for {weapon_stats['Duration']}")
    effect_name = weapon_stats["Ability Name"]
    duration = weapon_stats["Duration"]
    if effect_name in monster_on_going_effects:
        user_on_going_effects[effect_name]["Duration"] += duration
    else:
        user_on_going_effects[effect_name] = {
            "Amount": True, "Duration": weapon_stats["Duration"], "Item": weapon}

# Magic wand ability


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


def thunder_strike_ability(target, weapon):

    weapon_stats = All_items[weapon]
    weapon_trigger_chance = weapon_stats["Trigger Chance"]

    if random_chance(weapon_trigger_chance):
        type_effect(f"Triggering {weapon_stats['Ability Name']}!")
        type_effect(
            f"You dealt {weapon_stats['Extra Damage']} damage to the {target['Name']}")
        print()
        target["Health"] -= weapon_stats["Extra Damage"]


# Dual dagger ability
def extra_attack_ability(target, weapon):
    # This ability might be based on turn count rather than chance
    return


# Banana ability
def make_enemy_slip_ability(target, weapon):
    weapon_stats = All_items[weapon]
    weapon_trigger_chance = weapon_stats["Trigger Chance"]

    if random_chance(weapon_trigger_chance):
        type_effect(
            f"The enemy has slipped and hit its head.. He won't be able to move for {weapon_stats['Duration']} turns.")
        effect_name = weapon_stats["Ability Name"]
        duration = weapon_stats["Duration"]
        if effect_name in monster_on_going_effects:
            monster_on_going_effects[effect_name]["Duration"] += duration
        else:
            monster_on_going_effects[effect_name] = {
                "Amount": True, "Duration": weapon_stats["Duration"], "Item": weapon}
    else:
        type_effect("The cast has been unsuccessful...")


def distract_enemy_ability(target, weapon):
    pass

# Bubble Blower ability


def trap_enemy_ability(target, weapon):
    weapon_stats = All_items[weapon]
    weapon_trigger_chance = weapon_stats["Trigger Chance"]
    if random_chance(weapon_trigger_chance):
        type_effect(
            f"The enemy has been trapped for {weapon_stats['Duration']} turns.")
        effect_name = weapon_stats["Ability Name"]
        duration = weapon_stats["Duration"]
        if effect_name in monster_on_going_effects:
            monster_on_going_effects[effect_name]["Duration"] += duration
        else:
            monster_on_going_effects[effect_name] = {
                "Amount": True, "Duration": weapon_stats["Duration"], "Item": weapon}
    else:
        type_effect("The cast has been unsuccessful...")


# Magic Yo-Yo ability
def return_strike_ability(user, target):
    # Assuming 'Magic Yo-Yo' weapon
    pass


def entangle_enemy_ability(target, weapon):
    weapon_trigger_chance = All_items[weapon]["Trigger Chance"]
    if random_chance(weapon_trigger_chance):
        monster_on_going_effects["Trapped"]["Duration"] = All_items[weapon]["Duration"]
        monster_on_going_effects["Trapped"]["Amount"] = True
    pass


def squeak_noise_ability(target, weapon):
    type_effect("*Squeek*")
    pass


def rapid_fire_ability(target, weapon):
    # Assuming 'AK-47' weapon
    pass


def soft_block_ability(target, weapon, damage=0):
    weapon_trigger_chance = All_items[weapon]["Trigger Chance"]
    if random_chance(weapon_trigger_chance):
        print("Triggering shield special ability")
        damage_reduced = math.ceil(
            damage*(All_items[weapon]["Damage Reduction"] / 100))
        type_effect(
            f"{All_items[weapon]['Ability Name']} Activated: {damage_reduced} reduced!")
        new_damage = damage - damage_reduced
        print()
        return new_damage
    else:
        return damage


def knowledge_strike_ability(user, target):
    # Assuming 'Book' weapon
    # Logic for revealing clues or spells
    pass


def stealth_mode_ability(user, target):
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


def trigger_weapon_shield_ability(target, type=0, damage=0):
    # Type 0 for weapon, type 1 for shield
    weapon_types = ["Weapon", "Shield"]
    weapon_type = weapon_types[type]

    equipped_weapon_name = equiped_gear.get(weapon_type)
    if equipped_weapon_name is not None:
        print(f"Equipped {weapon_type}: {equipped_weapon_name}")

        item_trigger_ability = item_abilities.get(equipped_weapon_name)

        if weapon_type == "Weapon":
            print("Triggering weapon ability")
            item_trigger_ability(target, equipped_weapon_name)

        elif item_trigger_ability is not None and "Special Trigger" in All_items[equipped_weapon_name]:
            print("Triggering shield special ability")
            return item_trigger_ability(target, equipped_weapon_name, damage)
        else:
            print("No valid trigger condition")
    else:
        print(f"No {weapon_type} equipped")
