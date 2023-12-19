from Game_Structure.monster_abilities import *


def reset_enemies():
    # Regular Enemies

    global regular_enemies
    global bosses

    for enemy_name, stats in regular_enemies.items():

        if stats["Health"] < 0:
            regular_enemies[enemy_name]["Health"] = Base_Health_Values[enemy_name]


Base_Health_Values = {
    "Shadow Thief": 60,
    "Goblin Engineer": 50,
    "Mystic Sorcerer": 70,
    "Lich King": 150,
    "Fire Breathing Dragon": 200
}


# Regular Enemies
regular_enemies = {
    "Shadow Thief": {
        "Type": "Regular",
        "Health": 60,
        "Attack": 15,
        "Defence": 5,
        "Dodge": 30,
        "Name": "Shadow Thief"
    },
    "Goblin Engineer": {
        "Type": "Regular",
        "Health": 50,
        "Attack": 20,
        "Defence": 15,
        "Dodge": 5,
        "Name": "Goblin Engineer"
    },
    "Mystic Sorcerer": {
        "Type": "Regular",
        "Health": 70,
        "Attack": 18,
        "Defence": 12,
        "Dodge": 5,
        "Name": "Mystic Sorcerer"
    }
}


# Bosses
bosses = {
    "Lich King": {
        "Type": "Boss",
        "Health": 150,
        "Attack": 30,
        "Defence": 25,
        "Dodge": 10,
        "Name": "Lich King"
    },
    "Fire-Breathing Dragon": {
        "Type": "Boss",
        "Health": 200,
        "Attack": 40,
        "Defence": 20,
        "Dodge": 10,  # Assuming dodge value for the dragon, add if necessary
        "Name": "Fire-Breathing Dragon"
    },

    # Currently only the two bosses above exist in the game
}
