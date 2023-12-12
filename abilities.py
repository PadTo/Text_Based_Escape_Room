import random
from effects import *
from items import *
from inventory import *
from stats import *
from character import equiped_gear, character_stats
import math

# This is because the combat currently only accounts for e.g. 3 rounds when an effect has to continue for 4 rounds


def duration_mod(duration):
    duration += 1
    return duration


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


def freeze_ability(target, weapon, damage=0):
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


def double_damage_ability(target, weapon, damage=0):
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


def silence_ability(target, weapon, damage=0):
    weapon_stats = All_items[weapon]
    effect_name = weapon_stats["Ability Name"]
    duration = weapon_stats["Duration"]
    if user_cooldowns[effect_name]["Cooldown"] <= 0:

        type_effect(
            f"The enemy has been silenced for {weapon_stats['Duration']} turns.")
        user_cooldowns[effect_name] = {
            "Cooldown": weapon_stats["Cooldown"], "Item": weapon}
        if effect_name in monster_on_going_effects:
            monster_on_going_effects[effect_name]["Duration"] += duration_mod(
                duration)
        else:
            monster_on_going_effects[effect_name] = {
                "Amount": True, "Duration": duration_mod(duration), "Item": weapon}
    else:
        type_effect(f"{effect_name} is on cooldown...")
        type_effect("Choose another action:")
        return False
# Magic wand ability


def cast_random_spell_ability(target, weapon, damage=0):
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


def thunder_strike_ability(target, weapon, damage=0):

    weapon_stats = All_items[weapon]
    weapon_trigger_chance = weapon_stats["Trigger Chance"]

    if random_chance(weapon_trigger_chance):
        type_effect(f"Triggering {weapon_stats['Ability Name']}!")
        type_effect(
            f"You dealt {weapon_stats['Extra Damage']} damage to the {target['Name']}")
        print()
        target["Health"] -= weapon_stats["Extra Damage"]


# Banana ability
def make_enemy_slip_ability(target, weapon, damage=0):
    weapon_stats = All_items[weapon]
    weapon_trigger_chance = weapon_stats["Trigger Chance"]
    duration = weapon_stats["Duration"]

    if random_chance(weapon_trigger_chance):
        type_effect(
            f"The enemy has slipped and hit its head.. He won't be able to move for {duration} turns.")
        effect_name = weapon_stats["Ability Name"]
        if effect_name in monster_on_going_effects:
            monster_on_going_effects[effect_name]["Duration"] += duration_mod(
                duration)
        else:
            monster_on_going_effects[effect_name] = {
                "Amount": True, "Duration": duration_mod(duration), "Item": weapon}
    else:
        type_effect("The cast has been unsuccessful...")


# Bubble Blower ability


def trap_enemy_ability(target, weapon, damage=0):
    weapon_stats = All_items[weapon]
    effect_name = weapon_stats["Ability Name"]
    duration = weapon_stats["Duration"]

    if user_cooldowns[effect_name]["Cooldown"] <= 0:

        weapon_trigger_chance = weapon_stats["Trigger Chance"]
        if random_chance(weapon_trigger_chance):
            type_effect(
                f"The enemy has been trapped for {duration} turns.")
            user_cooldowns[effect_name] = {
                "Cooldown": duration_mod(weapon_stats["Cooldown"]), "Item": weapon}
            if effect_name in monster_on_going_effects:
                monster_on_going_effects[effect_name]["Duration"] += duration_mod(
                    duration)
            else:
                monster_on_going_effects[effect_name] = {
                    "Amount": True, "Duration": duration_mod(duration), "Item": weapon}

        else:
            type_effect("The cast has been unsuccessful...")
    else:
        type_effect(f"{effect_name} is on cooldown...")
        type_effect("Choose another action:")
        return False


# Magic Yo-Yo ability
def return_strike_ability(target, weapon, damage):
    weapon_stats = All_items[weapon]
    weapon_trigger_chance = weapon_stats["Trigger Chance"]
    if random_chance(weapon_trigger_chance):
        type_effect(
            f"You have dealt {damage} to the {target['Name']}")
        target["Health"] -= damage
        type_effect(f"Remaining {target['Name']} health: {target['Health']}")

        print()
        type_effect(f"Triggering {weapon_stats['Ability Name']}!")

# Spaghetti Whip ability


def entangle_enemy_ability(target, weapon, damage=0):
    weapon_stats = All_items[weapon]
    duration = weapon_stats["Duration"]
    weapon_trigger_chance = All_items[weapon]["Trigger Chance"]
    if random_chance(weapon_trigger_chance):
        type_effect(
            f"The enemy has been entangled for {duration} turns.")
        monster_on_going_effects["Trap"] = {
            "Amount": True, "Duration": duration_mod(duration), "Item": weapon}


def squeak_noise_ability(target, weapon, damage):
    type_effect("*Squeek*")


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


def stealth_mode_ability(target, weapon, damage=0):

    weapon_stats = All_items[weapon]
    effect_name = weapon_stats["Ability Name"]
    duration = weapon_stats["Duration"]

    if user_cooldowns[effect_name]["Cooldown"] <= 0:

        type_effect(f"Casting {effect_name}!")
        user_cooldowns[effect_name] = {
            "Cooldown": duration_mod(weapon_stats["Cooldown"]), "Item": weapon}
        print()

        if effect_name in user_on_going_effects:
            user_on_going_effects[effect_name]["Duration"] += duration
        else:
            user_on_going_effects[effect_name] = {
                "Amount": True, "Duration": duration, "Item": weapon}
    else:
        type_effect(f"{effect_name} is on cooldown...")
        type_effect("Choose another action:")
        return False


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

        stat_increase(potion)


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
    "Banana Peel": make_enemy_slip_ability,
    "Spaghetti Whip": entangle_enemy_ability,
    "Magic Yo-Yo": return_strike_ability,
    "Bubble Blower": trap_enemy_ability,
    "Squeaky Hammer": squeak_noise_ability,
    "Pillow": soft_block_ability,
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
        # print(f"Equipped {weapon_type}: {equipped_weapon_name}")

        item_trigger_ability = item_abilities.get(equipped_weapon_name)

        if weapon_type == "Weapon" and "Special Trigger" in All_items[equipped_weapon_name]:
            # print("Triggering weapon ability")
            item_trigger_ability(target, equipped_weapon_name, damage)

        elif item_trigger_ability is not None and "Special Trigger" in All_items[equipped_weapon_name]:
            # print("Triggering shield special ability")
            return item_trigger_ability(target, equipped_weapon_name, damage)
        else:
            # print("No valid trigger condition")
            pass
    else:
        # print(f"No {weapon_type} equipped")
        pass
