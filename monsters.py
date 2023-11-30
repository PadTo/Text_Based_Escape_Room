from monster_abilities import *

# Regular Enemies
regular_enemies = {
    "Shadow Thief": {
        "Type": "Regular",
        "Health": 60,
        "Attack Damage": 15,
        "Defence": 10,
        "Special Ability": shadow_thief_ability
    },
    "Goblin Engineer": {
        "Type": "Regular",
        "Health": 50,
        "Attack Damage": 20,
        "Defence": 15,
        "Special Ability": goblin_engineer_ability
    },
    "Mystic Sorcerer": {
        "Type": "Regular",
        "Health": 70,
        "Attack Damage": 18,
        "Defence": 12,
        "Special Ability": mystic_sorcerer_ability
    },
    "Armored Knight": {
        "Type": "Regular",
        "Health": 80,
        "Attack Damage": 25,
        "Defence": 30,
        "Special Ability": armored_knight_ability
    },
    "Sneaky Assassin": {
        "Type": "Regular",
        "Health": 55,
        "Attack Damage": 30,
        "Defence": 8,
        "Special Ability": sneaky_assassin_ability
    }
}

# Bosses
bosses = {
    "Lich King": {
        "Type": "Boss",
        "Health": 150,
        "Attack Damage": 35,
        "Defence": 25,
        "Special Abilities": lich_king_ability,
        "Name": "Lich King"
    },
    "Fire-Breathing Dragon": {
        "Type": "Boss",
        "Health": 200,
        "Attack Damage": 40,
        "Defence": 20,
        "Special Abilities": fire_breathing_dragon_ability,
        "Name": "Fire-Breathing Dragon"
    },
    "Mechanical Overlord": {
        "Type": "Boss",
        "Health": 180,
        "Attack Damage": 30,
        "Defence": 35,
        "Special Abilities": mechanical_overlord_ability,
        "Name": "Mechanical Overlord"
    },
    "Queen of Shadows": {
        "Type": "Boss",
        "Health": 130,
        "Attack Damage": 25,
        "Defence": 18,
        "Special Abilities": queen_of_shadows_ability,
        "Name": "Queen of Shadows"
    },
    "Ancient Stone Golem": {
        "Type": "Boss",
        "Health": 250,
        "Attack Damage": 30,
        "Defence": 40,
        "Special Abilities": ancient_stone_golem_ability,
        "Name": "Ancient Stone Golem"
    }
}
