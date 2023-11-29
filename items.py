from abilities import *
# Weapon Items
Weapons = {
    "Frostmourne": {
        "type": "Weapon",
        "weapon_type": "Sword",
        "attack_damage": 50,
        "special_trigger_ability": "20% chance to freeze the enemy for 1 turn"
    },
    "AK-47": {
        "type": "Weapon",
        "weapon_type": "Gun",
        "attack_damage": 35,  # per shot
        "ammo_capacity": 30,
        "note": "Requires ammo to use"
    },
    "Ashbringer": {
        "type": "Weapon",
        "weapon_type": "Sword",
        "attack_damage": 45,
        "special_trigger_ability": "15% chance to deal double damage"
    },
    "Skeleton Shield": {
        "type": "Weapon",
        "weapon_type": "Shield",
        "defence": 25,
        "special_trigger_ability": "10% chance to reflect 25% of the damage back to the attacker"
    },
    "Wooden Shield": {
        "type": "Weapon",
        "weapon_type": "Shield",
        "defence": 15,
        "durability": "Moderate (can break after extensive use)"
    },
    "Pillow": {
        "type": "Weapon",
        "weapon_type": "Defence Item",
        "defence": 5,
        "note": "Mostly for fun, low practical use"
    },
    "Book": {
        "type": "Weapon",
        "weapon_type": "Misc",
        "attack_damage": 10,  # when thrown
        "special_use": "Can contain clues or spells"
    },
    "Rock": {
        "type": "Weapon",
        "weapon_type": "Thrown",
        "attack_damage": 15
    },
    "Crossbow of Silence": {
        "type": "Weapon",
        "weapon_type": "Crossbow",
        "attack_damage": 30,
        "special_cast_ability": "Silences the enemy for 2 turns, preventing them from using special abilities"
    },
    "Mystic Wand": {
        "type": "Weapon",
        "weapon_type": "Wand",
        "attack_damage": 20,
        "special_trigger_ability": "25% chance to cast a random spell (e.g., fireball, healing, stun)"
    },
    "Thunder Hammer": {
        "type": "Weapon",
        "weapon_type": "Hammer",
        "attack_damage": 40,
        "special_trigger_ability": "15% chance to summon a thunder strike, dealing extra 20 damage"
    },
    "Dual Daggers": {
        "type": "Weapon",
        "weapon_type": "Dagger",
        "attack_damage": 25,  # combined
        "special_trigger_ability": "Grants an extra attack every third turn"
    },
    "Banana Peel": {
        "type": "Weapon",
        "weapon_type": "Whacky",
        "attack_damage": 5,
        "special_trigger_ability": "50% chance to make the enemy slip, causing them to lose a turn"
    },
    "Rubber Chicken": {
        "type": "Weapon",
        "weapon_type": "Whacky",
        "attack_damage": 10,
        "special_cast_ability": "Can be used to distract enemies, increasing your dodge chance by 30% for 1 turn"
    },
    "Spaghetti Whip": {
        "type": "Weapon",
        "weapon_type": "Whacky",
        "attack_damage": 15,
        "special_ability": "20% chance to entangle the enemy, reducing their attack damage by 10 for 2 turns"
    },
    "Magic Yo-Yo": {
        "type": "Weapon",
        "weapon_type": "Whacky",
        "attack_damage": 20,
        "special_ability": "30% chance to return to the player after an attack, allowing for an immediate second strike"
    },
    "Bubble Blower": {
        "type": "Weapon",
        "weapon_type": "Whacky",
        "attack_damage": 12,
        "special_cast_ability": "Blows bubbles that have a 25% chance to trap the enemy for 1 turn"
    },
    "Squeaky Hammer": {
        "type": "Weapon",
        "weapon_type": "Whacky",
        "attack_damage": 18,
        "special_trigger_ability": "Makes a squeaking sound"
    }

}

Armor = {
    "Iron Helm": {
        "type": "Helm",
        "defence": 15,
        "speed_effect": None
    },
    "Leather Cap": {
        "type": "Helm",
        "defence": 10,
        "speed_effect": "Increases dodge chance by 5%"
    },
    "Steel Helm": {
        "type": "Helm",
        "defence": 20,
        "speed_effect": "Reduces speed slightly"
    },
    "Chainmail": {
        "type": "Body Armor",
        "defence": 30,
        "speed_effect": "Reduces speed"
    },
    "Leather Armor": {
        "type": "Body Armor",
        "defence": 20,
        "speed_effect": "No speed reduction"
    },
    "Plate Armor": {
        "type": "Body Armor",
        "defence": 40,
        "speed_effect": "Significantly reduces speed"
    },
    "Blanket": {
        "type": "Misc",
        "defence": 5,
        "special_use": "Can be used for stealth or disguise"
    },
    "Leather Boots": {
        "type": "Footwear",
        "defence": 10,
        "speed_effect": "No speed reduction"
    },
    "Steel-toed Boots": {
        "type": "Footwear",
        "defence": 15,
        "speed_effect": "Reduces speed slightly"
    },
    "Sneakers": {
        "type": "Footwear",
        "defence": 5,
        "speed_effect": "Increases speed"
    }
}

Potions = {
    "Potion of Health": {
        "type": "Potion",
        "small": {
            "health_boost": 20
        },
        "medium": {
            "health_boost": 50
        },
        "large": {
            "health_boost": 100
        }
    },
    "Potion of Dodge Chance": {
        "type": "Potion",
        "effect": "Increases dodge chance by 20%",
        "duration": "3 turns"
    },
    "Potion of Defence": {
        "effect": "Increases defence by 30",
        "duration": "5 turns"
    },
    "Potion of Greed": {
        "type": "Potion",
        "effect": "Doubles any loot found",
        "side_effect": "Reduces defence by 10",
        "duration": "2 turns"
    },
    "Potion of the Unknown": {
        "type": "Potion",
        "effect": "Random (could be beneficial or detrimental)"
    }
}

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
    "Squeaky Hammer": squeak_noise_ability
    # Continue mapping other weapons to their abilities
}


All_items = {
    "Frostmourne": {
        "type": "Weapon",
        "weapon_type": "Sword",
        "attack_damage": 50,
        "special_trigger_ability": "20% chance to freeze the enemy for 1 turn"
    },
    "AK-47": {
        "type": "Weapon",
        "weapon_type": "Gun",
        "attack_damage": 35,  # per shot
        "ammo_capacity": 30,
        "note": "Requires ammo to use"
    },
    "Ashbringer": {
        "type": "Weapon",
        "weapon_type": "Sword",
        "attack_damage": 45,
        "special_trigger_ability": "15% chance to deal double damage"
    },
    "Skeleton Shield": {
        "type": "Weapon",
        "weapon_type": "Shield",
        "defence": 25,
        "special_trigger_ability": "10% chance to reflect 25% of the damage back to the attacker"
    },
    "Wooden Shield": {
        "type": "Weapon",
        "weapon_type": "Shield",
        "defence": 15,
        "durability": "Moderate (can break after extensive use)"
    },
    "Pillow": {
        "type": "Weapon",
        "weapon_type": "Defence Item",
        "defence": 5,
        "note": "Mostly for fun, low practical use"
    },
    "Book": {
        "type": "Weapon",
        "weapon_type": "Misc",
        "attack_damage": 10,  # when thrown
        "special_use": "Can contain clues or spells"
    },
    "Rock": {
        "type": "Weapon",
        "weapon_type": "Thrown",
        "attack_damage": 15
    },
    "Crossbow of Silence": {
        "type": "Weapon",
        "weapon_type": "Crossbow",
        "attack_damage": 30,
        "special_cast_ability": "Silences the enemy for 2 turns, preventing them from using special abilities"
    },
    "Mystic Wand": {
        "type": "Weapon",
        "weapon_type": "Wand",
        "attack_damage": 20,
        "special_trigger_ability": "25% chance to cast a random spell (e.g., fireball, healing, stun)"
    },
    "Thunder Hammer": {
        "type": "Weapon",
        "weapon_type": "Hammer",
        "attack_damage": 40,
        "special_trigger_ability": "15% chance to summon a thunder strike, dealing extra 20 damage"
    },
    "Dual Daggers": {
        "type": "Weapon",
        "weapon_type": "Dagger",
        "attack_damage": 25,  # combined
        "special_trigger_ability": "Grants an extra attack every third turn"
    },
    "Banana Peel": {
        "type": "Weapon",
        "weapon_type": "Whacky",
        "attack_damage": 5,
        "special_trigger_ability": "50% chance to make the enemy slip, causing them to lose a turn"
    },
    "Rubber Chicken": {
        "type": "Weapon",
        "weapon_type": "Whacky",
        "attack_damage": 10,
        "special_cast_ability": "Can be used to distract enemies, increasing your dodge chance by 30% for 1 turn"
    },
    "Spaghetti Whip": {
        "type": "Weapon",
        "weapon_type": "Whacky",
        "attack_damage": 15,
        "special_ability": "20% chance to entangle the enemy, reducing their attack damage by 10 for 2 turns"
    },
    "Magic Yo-Yo": {
        "type": "Weapon",
        "weapon_type": "Whacky",
        "attack_damage": 20,
        "special_ability": "30% chance to return to the player after an attack, allowing for an immediate second strike"
    },
    "Bubble Blower": {
        "type": "Weapon",
        "weapon_type": "Whacky",
        "attack_damage": 12,
        "special_cast_ability": "Blows bubbles that have a 25% chance to trap the enemy for 1 turn"
    },
    "Squeaky Hammer": {
        "type": "Weapon",
        "weapon_type": "Whacky",
        "attack_damage": 18,
        "special_trigger_ability": "Makes a squeaking sound"
    },



    "Iron Helm": {
        "type": "Helm",
        "defence": 15,
        "speed_effect": None
    },
    "Leather Cap": {
        "type": "Helm",
        "defence": 10,
        "speed_effect": "Increases dodge chance by 5%"
    },
    "Steel Helm": {
        "type": "Helm",
        "defence": 20,
        "speed_effect": "Reduces speed slightly"
    },
    "Chainmail": {
        "type": "Body Armor",
        "defence": 30,
        "speed_effect": "Reduces speed"
    },
    "Leather Armor": {
        "type": "Body Armor",
        "defence": 20,
        "speed_effect": "No speed reduction"
    },
    "Plate Armor": {
        "type": "Body Armor",
        "defence": 40,
        "speed_effect": "Significantly reduces speed"
    },
    "Blanket": {
        "type": "Misc",
        "defence": 5,
        "special_use": "Can be used for stealth or disguise"
    },
    "Leather Boots": {
        "type": "Footwear",
        "defence": 10,
        "speed_effect": "No speed reduction"
    },
    "Steel-toed Boots": {
        "type": "Footwear",
        "defence": 15,
        "speed_effect": "Reduces speed slightly"
    },
    "Sneakers": {
        "type": "Footwear",
        "defence": 5,
        "speed_effect": "Increases speed"
    },


    "Potion of Health": {
        "type": "Potion",
        "small": {
            "health_boost": 20
        },
        "medium": {
            "health_boost": 50
        },
        "large": {
            "health_boost": 100
        }
    },
    "Potion of Dodge Chance": {
        "type": "Potion",
        "effect": "Increases dodge chance by 20%",
        "duration": "3 turns"
    },
    "Potion of Defence": {
        "effect": "Increases defence by 30",
        "duration": "5 turns"
    },
    "Potion of Greed": {
        "type": "Potion",
        "effect": "Doubles any loot found",
        "side_effect": "Reduces defence by 10",
        "duration": "2 turns"
    },
    "Potion of the Unknown": {
        "type": "Potion",
        "effect": "Random (could be beneficial or detrimental)"
    }

}
