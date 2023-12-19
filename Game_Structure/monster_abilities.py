
from Game_Structure.text_effect import type_effect
from Game_Structure.character import character_stats
from Game_Structure.effects import user_on_going_effects, monster_cooldowns
from Game_Structure.stats import stat_increase, stat_decrease


def duration_mod(duration):
    duration += 1
    return duration


def attack():
    return "Attack"


# Shadow Thief Abilities


def shadow_thief_shadow_step(target, monster):
    back_stab_dmg = 20
    attack_reduction = 10
    cooldown_duration = duration_mod(4)

    # Initialize cooldown if it doesn't exist
    if "Back Stab" not in monster_cooldowns:
        monster_cooldowns["Back Stab"] = {"Cooldown": 0}

    if monster_cooldowns["Back Stab"]["Cooldown"] <= 0:
        type_effect(
            f"The {monster['Name']} has teleported behind you!. {monster['Name']} uses back-stab.")
        character_stats["Health"] -= back_stab_dmg

        type_effect(
            f"{back_stab_dmg} damage taken. Current Health: {character_stats['Health']}.")

        # Apply attack reduction
        user_on_going_effects["Attack Reduction"] = {
            "Amount": -attack_reduction, "Duration": 4, "Item": "Shadow Thief's Daggers"}

        stat_decrease("Shadow Thief's Daggers")

        type_effect(f"Reduced attack for 4 rounds.")
        print()

        # Set cooldown for the ability
        monster_cooldowns["Back Stab"]["Cooldown"] = cooldown_duration
        return True
    else:
        return False


def shadow_thief_disarm(target, monster):

    cooldown_duration = duration_mod(5)
    disarm_duration = 2

    # Initialize cooldown if it doesn't exist
    if "Disarm" not in monster_cooldowns:
        monster_cooldowns["Disarm"] = {"Cooldown": 0}

    if monster_cooldowns["Disarm"]["Cooldown"] <= 0:
        type_effect(
            f"You have been temporarily disarmed for {disarm_duration} rounds...")

        # Apply disarm
        user_on_going_effects["Disarm"] = {
            "Amount": True, "Duration": duration_mod(disarm_duration), "Item": {}}

        # Set cooldown for the ability
        monster_cooldowns["Disarm"]["Cooldown"] = cooldown_duration
        return True
    else:
        return False

# Goblin Engineer Abilities


def goblin_engineer_mechanical_fix(target, self):
    # Repairs or buffs mechanical units
    pass


def goblin_engineer_turret_deploy(target, self):
    # Deploys a stationary turret
    pass

# Mystic Sorcerer Abilities


def mystic_sorcerer_arcane_blast(target, self):
    # Strong magical attack against the target
    pass


def mystic_sorcerer_spell_barrier(target, self):
    # Shields from attacks
    pass

# Lich King Abilities


def lich_king_necrotic_pulse(target, self):
    # Area-of-effect damage
    pass


def lich_king_soul_drain(target, self):
    # Drains health from the player
    pass

# Fire-Breathing Dragon Abilities


def dragon_inferno_breath(target, self):
    # Powerful fire attack
    pass


def dragon_wing_gust(target, self):
    # Knocks back and damages the player
    pass


enemy_abilities = {

    # Regular enemies
    "Shadow Thief": {
        "Basic Attack": attack,
        "Shadow Step": shadow_thief_shadow_step,  # Teleports and strikes
        "Disarm": shadow_thief_disarm  # Temporarily disarms the player
    },
    "Goblin Engineer": {
        "Basic Attack": attack,
        "Mechanical Fix": goblin_engineer_mechanical_fix,
        "Turret Deploy": goblin_engineer_turret_deploy
    },
    "Mystic Sorcerer": {
        "Basic Attack": attack,
        "Arcane Blast": mystic_sorcerer_arcane_blast,  # Strong magical attack
        "Spell Barrier": mystic_sorcerer_spell_barrier  # Shields from attacks
    },


    # Bosses
    "Lich King": {
        "Basic Attack": attack,
        "Necrotic Pulse": lich_king_necrotic_pulse,  # Area-of-effect damage
        "Soul Drain": lich_king_soul_drain  # Drains health from the player
    },
    "Fire-Breathing Dragon": {
        "Basic Attack": attack,
        "Inferno Breath": dragon_inferno_breath,  # Powerful fire attack
        "Wing Gust": dragon_wing_gust  # Knocks back and damages the player
    },

}


def available_monster_ability(attacker):
    abilities = enemy_abilities[attacker["Name"]]
    available_abilities = [ability for ability in abilities if monster_cooldowns.get(
        ability, {"Cooldown": 0})["Cooldown"] <= 0]
    return available_abilities
