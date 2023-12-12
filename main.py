

# Stat decrease/increase don't work properly


import random

# Import necessary modules and functions
from text_effect import type_effect
from combat import combat
from items import All_items
from inventory import add_item_to_inventory, display_inventory
from character import character_stats
from monsters import regular_enemies


def main():
    player = character_stats
    game_state = "Exploration"

    type_effect("Welcome to the mystical world of Eldoria!")
    type_effect("You find yourself at a crossroads in a dense forest.")

    while game_state != "End":
        type_effect("\nWhat would you like to do?")
        type_effect("1: Explore the forest")
        type_effect("2: Check your inventory")
        type_effect("3: Solve the riddle from the ancient statue")
        type_effect("4: End game")
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            encounter_forest(player)
        elif choice == "2":
            display_inventory()
        elif choice == "3":
            solve_riddle(player)
        elif choice == "4":
            type_effect("Thank you for playing!")
            game_state = "End"
        else:
            type_effect("Invalid choice, please choose again.")


def encounter_forest(player):
    type_effect(
        "While exploring, you stumble upon a hidden enemy - the Shadow Thief!")
    monster = regular_enemies["Shadow Thief"]
    combat(player, monster, "Combat")


def solve_riddle(player):
    type_effect("You approach the ancient statue and read the riddle.")
    riddle = "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?"
    type_effect(riddle)
    answer = input("Enter your answer: ").lower()

    if answer == "echo":
        type_effect("Correct! The statue reveals a hidden cache of items.")
        print()
        add_item_to_inventory("Potion of Greed", 3)
        add_item_to_inventory("Mystic Wand", 1)
    else:
        type_effect("Incorrect. The statue remains silent.")


if __name__ == "__main__":
    main()
