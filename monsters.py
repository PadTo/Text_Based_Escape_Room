from monster_abilities import *


def reset_enemies():
    # Regular Enemies

    global regular_enemies
    global bosses
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
