import random as rand
import numpy as np

import character
from text_effect import type_effect
from items import *
from inventory import *
from combat import *
from constants import *
from display_effect import display_effects

add_item_to_inventory("Ashbringer", 1)
add_item_to_inventory("Mystic Wand", 1)
add_item_to_inventory("Frostmourne", 1)
add_item_to_inventory("Pillow", 1)
add_item_to_inventory("Skeleton Shield", 1)
add_item_to_inventory("Crossbow of Silence", 1)


add_item_to_inventory("Thunder Hammer", 1)
add_item_to_inventory("Spaghetti Whip", 1)  # Doesn't work
add_item_to_inventory("Magic Yo-Yo", 1)  # needs a bit of revamping
add_item_to_inventory("Bubble Blower", 1)  # Doesn't work
add_item_to_inventory("Squeaky Hammer", 1)
add_item_to_inventory("Blanket", 1)  # Doesn't work

equip("Blanket")


# display_inventory()
monster = bosses["Lich King"]
combat(character_stats, monster, game_state="Combat")
