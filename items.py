import random as rand

# Weapon Items
Weapons = {
    "Frostmourne": {
        "type": "Sword",
        "attack_damage": 50,
        "special_trigger_ability": "20% chance to freeze the enemy for 1 turn"
    },
    "AK-47": {
        "type": "Gun",
        "attack_damage": 35,  # per shot
        "ammo_capacity": 30,
        "note": "Requires ammo to use"
    },
    "Ashbringer": {
        "type": "Sword",
        "attack_damage": 45,
        "special_trigger_ability": "15% chance to deal double damage"
    },
    "Skeleton Shield": {
        "type": "Shield",
        "defence": 25,
        "special_trigger_ability": "10% chance to reflect 25% of the damage back to the attacker"
    },
    "Wooden Shield": {
        "type": "Shield",
        "defence": 15,
        "durability": "Moderate (can break after extensive use)"
    },
    "Pillow": {
        "type": "Defence Item",
        "defence": 5,
        "note": "Mostly for fun, low practical use"
    },
    "Book": {
        "type": "Misc",
        "attack_damage": 10,  # when thrown, if thrown removes from inventory
        "special_use": "Can contain clues or spells"
    },
    "Rock": {
        "type": "Thrown",
        "attack_damage": 15
    },
    "Crossbow of Silence": {
        "type": "Crossbow",
        "attack_damage": 30,
        # Does not work on bosses
        "special_cast_ability": "Silences the enemy for 2 turns, preventing them from using special abilities"
    },
    "Mystic Wand": {
        "type": "Wand",
        "attack_damage": 20,
        "special_trigger_ability": "25% chance to cast a random spell (e.g., fireball, healing, stun)"
    },
    "Thunder Hammer": {
        "type": "Hammer",
        "attack_damage": 40,
        "special_trigger_ability": "15% chance to summon a thunder strike, dealing extra 20 damage"
    },
    "Dual Daggers": {
        "type": "Dagger",
        "attack_damage": 25,  # combined
        "special_trigger_ability": "Grants an extra attack every third turn"
    },
    "Banana Peel": {
        "type": "Whacky",
        "attack_damage": 5,
        "special_trigger_ability": "50% chance to make the enemy slip, causing them to lose a turn"
    },
    "Rubber Chicken": {
        "type": "Whacky",
        "attack_damage": 10,
        "special_cast_ability": "Can be used to distract enemies, increasing your dodge chance by 30% for 2 turn"
    },
    "Spaghetti Whip": {
        "type": "Whacky",
        "attack_damage": 15,
        "special_ability": "20% chance to entangle the enemy, reducing their attack damage by 10 for 2 turns"
    },
    "Magic Yo-Yo": {
        "type": "Whacky",
        "attack_damage": 20,
        "special_ability": "30% chance to return to the player after an attack, allowing for an immediate second strike"
    },
    "Bubble Blower": {
        "type": "Whacky",
        "attack_damage": 12,
        "special_cast_ability": "Blows bubbles that have a 25% chance to trap the enemy for 2 turns"
    },
    "Squeaky Hammer": {
        "type": "Whacky",
        "attack_damage": 15,
        "special_trigger_ability": "Makes a squeaking sound"}
}


def special_ability(cast):
    pass


def special_ability_trigger():
    pass
