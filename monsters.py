from monster_abilities import *

# Regular Enemies
regular_enemies = {
    "Shadow Thief": {
        "Type": "Regular",
        "Health": 60,
        "Attack": 15,
        "Defence": 10,
        "Special Ability": shadow_thief_ability,
        "Name": "Shadow Thief"
    },
    "Goblin Engineer": {
        "Type": "Regular",
        "Health": 50,
        "Attack": 20,
        "Defence": 15,
        "Special Ability": goblin_engineer_ability,
        "Name": "Goblin Engineer"
    },
    "Mystic Sorcerer": {
        "Type": "Regular",
        "Health": 70,
        "Attack": 18,
        "Defence": 12,
        "Special Ability": mystic_sorcerer_ability,
        "Name": "Mystic Sorcerer"
    },
    "Armored Knight": {
        "Type": "Regular",
        "Health": 80,
        "Attack": 25,
        "Defence": 30,
        "Special Ability": armored_knight_ability,
        "Name": "Armored Knight"
    },
    "Sneaky Assassin": {
        "Type": "Regular",
        "Health": 55,
        "Attack": 30,
        "Defence": 8,
        "Special Ability": sneaky_assassin_ability,
        "Name": "Sneaky Assassin"
    }
}

# Bosses
bosses = {
    "Lich King": {
        "Type": "Boss",
        "Health": 150,
        "Attack": 100,
        "Defence": 25,
        "Dodge": 10,
        "Special Abilities": lich_king_ability,
        "Name": "Lich King"
    },
    "Fire-Breathing Dragon": {
        "Type": "Boss",
        "Health": 200,
        "Attack": 40,
        "Defence": 20,
        "Dodge": 10,  # Assuming dodge value for the dragon, add if necessary
        "Special Abilities": fire_breathing_dragon_ability,
        "Name": "Fire-Breathing Dragon"
    },
    "Mechanical Overlord": {
        "Type": "Boss",
        "Health": 180,
        "Attack": 30,
        "Defence": 35,
        "Dodge": 15,  # Assuming dodge value for the overlord, add if necessary
        "Special Abilities": mechanical_overlord_ability,
        "Name": "Mechanical Overlord"
    },
    "Queen of Shadows": {
        "Type": "Boss",
        "Health": 130,
        "Attack": 25,
        "Defence": 18,
        "Dodge": 20,  # Assuming dodge value for the queen, add if necessary
        "Special Abilities": queen_of_shadows_ability,
        "Name": "Queen of Shadows"
    },
    "Ancient Stone Golem": {
        "Type": "Boss",
        "Health": 250,
        "Attack": 30,
        "Defence": 40,
        "Dodge": 5,  # Assuming dodge value for the golem, add if necessary
        "Special Abilities": ancient_stone_golem_ability,
        "Name": "Ancient Stone Golem"
    }
}
