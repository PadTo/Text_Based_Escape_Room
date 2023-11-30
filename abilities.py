import random
from effects import *
from items import *
from inventory import *


def freeze_ability(user, target, game_state):
    # Logic for freeze ability
    pass


def double_damage_ability(user, target, game_state):
    # Logic for double damage ability
    pass


def reflect_damage_ability(user, target, game_state):
    # Logic for reflect damage ability
    pass


def silence_ability(user, target, game_state):
    # Logic for silence ability
    pass


def cast_random_spell_ability(user, target, game_state):
    # Logic for casting a random spell
    pass


def thunder_strike_ability(user, target, game_state):
    # Logic for thunder strike ability
    pass


def extra_attack_ability(user, target, game_state):
    # Logic for extra attack ability
    pass


def make_enemy_slip_ability(user, target, game_state):
    # Logic for making enemy slip
    pass


def distract_enemy_ability(user, target, game_state):
    # Logic for distracting enemy
    pass


def entangle_enemy_ability(user, target, game_state):
    # Logic for entangling enemy
    pass


def return_strike_ability(user, target, game_state):
    # Logic for return strike ability
    pass


def trap_enemy_ability(user, target, game_state):
    # Logic for trapping enemy
    pass


def squeak_noise_ability(user, target, game_state):
    # Logic for squeak noise
    pass


def rapid_fire_ability(user, target, game_state):
    # Logic for rapid fire ability
    pass


def rapid_fire_ability(user, target, game_state):
    # Logic for rapid fire ability
    pass


def soft_block_ability(user, target, game_state):
    # Logic for soft block ability
    pass


def knowledge_strike_ability(user, target, game_state):
    # Logic for knowledge strike ability
    pass


def stealth_mode_ability(user, target, game_state):
    # Logic for stealth mode ability
    pass


def increase_dodge_chance_potion_ability(potion, user, target, game_state):
    if game_state == "Combat" and potion == "Potion of Dodge Chance":
        used_potion = All_items[potion]

        effect_name = "Dodge Boost (Potion)"
        duration = used_potion["Duration"]
        boost_value = used_potion["Dodge"]

        # Update or add the effect in user_on_going_effects
        if effect_name in user_on_going_effects:
            user_on_going_effects[effect_name]["Amount"] += duration
        else:
            user_on_going_effects[effect_name] = {
                "Amount": boost_value, "Duration": duration, "Item": potion}

        # Apply the immediate effect (if any)
        stat_increase(potion)


def temporary_defence_boost_potion_ability(potion, user, target, game_state):
    if game_state == "Combat" and potion == "Potion of Defence":
        used_potion = All_items[potion]

        effect_name = "Defence Boost (Potion)"
        duration = used_potion["Duration"]
        boost_value = used_potion["Defence"]

        # Update or add the effect in user_on_going_effects
        if effect_name in user_on_going_effects:
            user_on_going_effects[effect_name]["Amount"] += duration
        else:
            user_on_going_effects[effect_name] = {
                "Amount": boost_value, "Duration": duration, "Item": potion}

        # Apply the immediate effect (if any)
        stat_increase(potion)


def greed_effect_potion_ability(potion, user, target, game_state):
    if game_state == "Combat" and potion == "Potion of Greed":
        used_potion = All_items[potion]

        effect_name = "Greed Effect (Potion)"
        duration = used_potion["Duration"]
        defence_penalty = used_potion["Defence"]

        user_on_going_effects[effect_name] = {
            "Amount": defence_penalty, "Duration": duration, "Item": potion}

        user_on_going_effects["Double Loot Boost"]["Duration"] += duration
        stat_decrease(potion)


def random_effect_potion_ability(potion, user, target, game_state):
    if game_state == "Combat" and potion == "Potion of the Unknown":
        possible_potions = ["Potion of Vulnerability", "Potion of Fortitude",
                            "Potion of Agility", "Potion of Clumsiness"]
        chosen_potion = random.choice(possible_potions)
        chosen_potion_stats = All_items[chosen_potion]

        effect_name = chosen_potion
        duration = chosen_potion_stats["Duration"]
        amount = chosen_potion_stats.get(
            "Defence", 0) or chosen_potion_stats.get("Dodge", 0)

        user_on_going_effects[effect_name] = {
            "Amount": amount, "Duration": duration, "Item": chosen_potion}

        # Apply the immediate effect (increase or decrease)
        if amount > 0:
            stat_increase(chosen_potion)
        else:
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

}
