from monster_abilities import *

# Regular Enemies
regular_enemies = {
    "Shadow Thief": {
        "Type": "Regular",
        "Health": 60,
        "Attack": 15,
        "Defence": 10,
        "Name": "Shadow Thief"
    },
    "Goblin Engineer": {
        "Type": "Regular",
        "Health": 50,
        "Attack": 20,
        "Defence": 15,
        "Name": "Goblin Engineer"
    },
    "Mystic Sorcerer": {
        "Type": "Regular",
        "Health": 70,
        "Attack": 18,
        "Defence": 12,
        "Name": "Mystic Sorcerer"
    }
}

# Bosses
bosses = {
    "Lich King": {
        "Type": "Boss",
        "Health": 15,
        "Attack": 0,
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
