from text_effect import type_effect
from items import All_items
from inventory import add_item_to_inventory
from combat import combat
from monsters import *


def visit_ancient_library(player):
    type_effect(
        "You arrive at the Ancient Library, a place filled with knowledge and mysteries.")
    type_effect(
        "As you enter, you notice two paths. One leads to the Hall of Tomes, the other to the Whispering Gallery.")
    type_effect("Which path do you choose? (tomes/gallery)")
    library_choice = input().lower()

    if library_choice == "tomes":
        explore_hall_of_tomes(player)
    elif library_choice == "gallery":
        explore_whispering_gallery(player)
    else:
        type_effect("Unable to decide, you leave the library for now.")

# Function to explore the Hall of Tomes


def explore_hall_of_tomes(player):
    type_effect(
        "The Hall of Tomes is vast, filled with ancient books and scrolls.")
    type_effect(
        "Among the dusty shelves, you find a peculiar book glowing faintly.")
    type_effect("Do you wish to read the book? (yes/no)")
    book_choice = input().lower()

    if book_choice == "yes":
        read_mysterious_book(player)
    else:
        type_effect(
            "You leave the book untouched and step back into the main hall.")

# Function to explore the Whispering Gallery


def explore_whispering_gallery(player):
    type_effect(
        "The Whispering Gallery is a circular room with walls echoing faint voices.")
    type_effect(
        "A puzzle lock guards a hidden chamber. Do you attempt to solve it? (yes/no)")
    puzzle_choice = input().lower()

    if puzzle_choice == "yes":
        solve_puzzle_lock(player)
    else:
        type_effect(
            "You decide not to meddle with the puzzle and notice a hidden passage.")
        explore_hidden_passage(player)


def explore_hidden_passage(player):
    type_effect("You cautiously walk down the hidden passage.")
    type_effect(
        "The passage leads to an underground garden, glowing with bioluminescent plants.")
    type_effect("In the garden, you find a chest. Do you open it? (yes/no)")
    garden_chest_choice = input().lower()

    if garden_chest_choice == "yes":
        open_garden_chest(player)
    else:
        type_effect("You leave the chest untouched and return to the library.")


def open_garden_chest(player):
    # Assuming 'Thunder Hammer' is an item in items.py
    if "Thunder Hammer" in All_items:
        type_effect(
            "Inside the chest, you find the Thunder Hammer, a weapon of immense power.")
        add_item_to_inventory(player, "Thunder Hammer", 1)
        type_effect(
            "With the Thunder Hammer in hand, you feel a surge of strength.")
    else:
        type_effect(
            "The chest is empty, leaving you curious about who might have taken the item.")
    return_to_library(player)


# Function to read the mysterious book


def read_mysterious_book(player):
    type_effect("As you open the book, you're sucked into a magical realm!")
    type_effect(
        "You find yourself in a mystical forest, with paths leading in different directions.")
    type_effect(
        "A signpost indicates two paths: 'Path of Wisdom' and 'Path of Courage'.")
    type_effect("Which path do you choose? (wisdom/courage)")
    path_choice = input().lower()

    if path_choice == "wisdom":
        path_of_wisdom(player)
    elif path_choice == "courage":
        path_of_courage(player)
    else:
        type_effect(
            "Unable to decide, a gust of wind guides you back to the library.")


def path_of_wisdom(player):
    type_effect(
        "You walk down the Path of Wisdom, surrounded by whispering trees.")
    # Assuming 'Mystic Wand' is an item in items.py
    if "Mystic Wand" in All_items:
        type_effect("You find the Mystic Wand, glowing with magical energy.")
        add_item_to_inventory("Mystic Wand", 1)
        type_effect("The Mystic Wand may help you in your quest.")
    else:
        type_effect(
            "The path ends abruptly, and you return to where you started.")
    # Returns the player to the library
    return_to_library(player)


def path_of_courage(player):
    type_effect(
        "The Path of Courage leads you into a clearing, where a creature awaits.")
    monster = regular_enemies["Shadow Thief"]
    type_effect(f"A {monster['Name']} challenges you!")
    combat(player, monster, "Combat")
    return_to_library(player)


def return_to_library(player):
    type_effect("A magical portal appears and takes you back to the library.")
    type_effect(
        "As you ponder your next steps, you notice an unusual flickering light behind a bookshelf.")
    type_effect("Do you investigate the light? (yes/no)")
    light_choice = input().lower()

    if light_choice == "yes":
        discover_hidden_labyrinth_entrance(player)
    else:
        type_effect("You decide to stay in the main area of the library.")


def discover_hidden_labyrinth_entrance(player):
    type_effect(
        "Pushing aside the bookshelf, you reveal a hidden passage leading down into darkness.")
    type_effect(
        "It seems to be an entrance to a labyrinth. Do you enter the labyrinth? (yes/no)")
    labyrinth_choice = input().lower()

    if labyrinth_choice == "yes":
        enter_labyrinth(player)
    else:
        type_effect(
            "You decide against venturing into the unknown and return to the safety of the library.")


def enter_labyrinth(player):
    type_effect(
        "You bravely step into the labyrinth. The path twists and turns, leading you deeper underground.")

    labyrinth_encounter(player)


def solve_puzzle_lock(player):
    type_effect(
        "You face the puzzle lock, inscribed with ancient runes. (α β ɣ)")
    correct_sequence = "alpha beta gamma"
    player_attempt = input("Enter the rune sequence: ")

    if player_attempt.lower() == correct_sequence:
        type_effect("The runes glow brightly and the lock opens.")
        discover_secret_chamber(player)
    else:
        type_effect("The runes flicker but remain locked.")
        type_effect("You step back, pondering your next move.")
        unsolved_puzzle_path(player)


def unsolved_puzzle_path(player):
    type_effect(
        "As you ponder your next move, a hidden panel in the wall slides open.")
    type_effect("Curious, you step through the panel into a dimly lit corridor.")
    type_effect(
        "The corridor leads to a mysterious room with an old book on a pedestal.")
    type_effect("Do you wish to examine the book? (yes/no)")
    book_choice = input().lower()

    if book_choice == "yes":
        examine_mysterious_book(player)
    else:
        type_effect(
            "You decide not to risk it and return to the Whispering Gallery.")


def examine_mysterious_book(player):
    type_effect(
        "As you open the book, the room illuminates with a magical light.")
    type_effect(
        "The book reveals the story of an ancient Eldorian hero and hints at a hidden treasure.")
    type_effect("Do you wish to seek this treasure? (yes/no)")
    treasure_choice = input().lower()

    if treasure_choice == "yes":
        seek_hidden_treasure(player)
    else:
        type_effect(
            "You close the book and the room dims. You decide to return to the Whispering Gallery.")


def seek_hidden_treasure(player):
    type_effect(
        "Guided by the book, you find yourself in a secret chamber beneath the library.")
    type_effect(
        "In the chamber, there is a treasure chest guarded by a spectral figure.")
    encounter_guardian(player)


def encounter_guardian(player):
    monster = regular_enemies["Shadow Thief"]
    type_effect(
        f"As you approach, the {monster['Name']} awakens, ready to defend the treasure.")
    combat(player, monster, "Combat")
    type_effect(
        "After a fierce battle, you defeat the guardian and approach the chest.")
    open_treasure_chest(player)


def open_treasure_chest(player):
    # Assuming 'Thunder Hammer' is an item in items.py
    if "Thunder Hammer" in All_items:
        type_effect(
            "Inside the chest, you find the Thunder Hammer, a weapon of immense power.")
        add_item_to_inventory(player, "Thunder Hammer", 1)
        type_effect("With the Thunder Hammer in hand, you feel unstoppable.")
    else:
        type_effect(
            "The chest is unfortunately empty. It seems someone else has claimed the treasure.")
    return_to_library(player)


def open_ancient_chest(player):

    if "Blanket" in All_items:
        type_effect(
            "Inside the chest, you find a Blanket.")
        add_item_to_inventory("Blanket", 1)
        type_effect(
            "With a Blanket in your possession, you feel much safer!")
    else:
        type_effect("The chest is empty, only cobwebs inside.")
    return_to_library(player)


def discover_secret_chamber(player):
    type_effect("Inside the chamber, you find a mysterious chest.")
    # Assuming 'Skeleton Shield' is an item in items.py
    if "Skeleton Shield" in All_items:
        type_effect(
            "You discover the Skeleton Shield, a rare and powerful artifact.")
        add_item_to_inventory("Skeleton Shield", 1)
        type_effect(
            "With the Skeleton Shield in your possession, you feel more protected.")
    else:
        type_effect("The chest is empty, perhaps someone else found it first.")
    # Returns the player to the library
    return_to_library(player)


def labyrinth_encounter(player):
    monster = regular_enemies["Shadow Thief"]
    type_effect(
        f"As you navigate the labyrinth, a {monster['Name']} ambushes you!")
    combat(player, monster, "Combat")
    type_effect("Victorious, you find a unique item on the ground.")
    # Assuming Magic Yo-Yo is in items.py
    add_item_to_inventory("Magic Yo-Yo", 1)
    type_effect(
        "You've obtained the Magic Yo-Yo, a whimsical yet powerful weapon.")
    print()
    type_effect("After the encounter, you notice a shimmering portal.")
    type_effect("Do you step through the portal? (yes/no)")
    portal_choice = input().lower()
    print()

    if portal_choice == "yes":
        step_through_portal(player)
    else:
        type_effect("You decide to stay and explore the labyrinth further.")
        print()


def step_through_portal(player):
    type_effect(
        "You step through the portal and find yourself in a secluded part of the library.")
    type_effect("A shadow moves quickly in the corner of your eye.")
    type_effect("Do you investigate the shadow? (yes/no)")
    shadow_choice = input().lower()
    print()

    if shadow_choice == "yes":
        shadow_encounter(player)
    else:
        type_effect(
            "You decide against investigating the shadow, feeling an eerie sense of danger.")
        type_effect("Suddenly, the portal flares up again.")
        type_effect("Do you step back through the portal to safety? (yes/no)")
        portal_return_choice = input().lower()

        if portal_return_choice == "yes":
            return_to_start(player)
        else:
            type_effect(
                "You choose to stay and explore this mysterious section of the library.")
            explore_secluded_library_section(player)


def return_to_start(player):
    type_effect(
        "You step back through the portal and find yourself at the start of your journey.")
    type_effect(
        "You gather your thoughts and decide on your next course of action.")
    print()


def explore_secluded_library_section(player):
    type_effect(
        "As you explore the secluded section, you come across an old tome.")
    type_effect(
        "The tome contains ancient knowledge that might aid you in your quest.")
    # Assuming 'Ancient Tome of Knowledge' is an item in items.py
    if "Ancient Tome of Knowledge" in All_items:
        add_item_to_inventory("Ancient Tome of Knowledge", 1)
        type_effect("You've obtained the Ancient Tome of Knowledge.")
    else:
        type_effect(
            "Although the tome crumbles to dust, the knowledge you gain is invaluable.")
    return_to_library(player)


def shadow_encounter(player):
    monster = regular_enemies["Shadow Thief"]
    type_effect(
        f"Suddenly, the {monster['Name']} leaps out from the shadows, ready to attack!")
    combat(player, monster, "Combat")
    type_effect("After defeating the Shadow Thief, you find a key he dropped.")
    add_item_to_inventory("Mysterious Key", 1)
    type_effect(
        "You've obtained a Mysterious Key, which might unlock new secrets.")
    investigate_secluded_area(player)


def investigate_secluded_area(player):
    type_effect(
        "With the Shadow Thief defeated, you take a moment to investigate the area.")
    type_effect("You discover a hidden compartment in one of the bookshelves.")
    type_effect("Using the Mysterious Key, you unlock the compartment.")
    find_hidden_compartment_treasure(player)


def find_hidden_compartment_treasure(player):
    if "Potion of Large Health" in All_items:
        type_effect(
            "Inside the compartment, you find a Large Potion of Health.")
        add_item_to_inventory("Potion of Large Health", 1)
        type_effect(
            "With the Potion of Large Health, you feel rejuvenated and ready for further adventures.")
    else:
        type_effect(
            "The compartment is empty, but you feel a sense of accomplishment for outsmarting the Shadow Thief.")
    return_to_library(player)
