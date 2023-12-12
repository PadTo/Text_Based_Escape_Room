

# Stat decrease/increase don't work properly


import random

# Import necessary modules and functions
from text_effect import type_effect
from combat import combat
from items import All_items
from inventory import add_item_to_inventory, display_inventory
from character import character_stats
from Maps.ancient_library import *


# Main function where the game starts
def main():
    player = character_stats
    game_state = "Exploration"

    type_effect("Welcome to the mystical world of Eldoria!")
    type_effect(
        "You stand at a crossroads in a dense forest, a map in your hand, and a sense of adventure in your heart.")

    while game_state != "End":
        type_effect("\nWhat would you like to do?")
        type_effect("1: Visit the Ancient Library")
        type_effect("2: Check your inventory")
        type_effect("3: End game")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            visit_ancient_library(player)
        elif choice == "2":
            display_inventory()
        elif choice == "3":
            type_effect("Thank you for playing! Farewell, adventurer.")
            game_state = "End"
        else:
            type_effect("Invalid choice, please choose again.")

# Ensure you have defined all other necessary functions and variables


if __name__ == "__main__":
    main()
