import random as rand
import numpy as np

import character
from text_effect import type_effect
from items import *
from inventory import *
from abilities import *
from combat import *
from constants import *
from display_effect import display_effects

add_item_to_inventory("Ashbringer", 1)
add_item_to_inventory("Mystic Wand", 1)
add_item_to_inventory("Frostmourne", 1)
add_item_to_inventory("Pillow", 1)
add_item_to_inventory("Skeleton Shield", 1)

display_inventory()
# equip("Ashbringer")
# equip("Mystic Wand")
# equip("Frostmourne")

monster = bosses["Lich King"]
combat(character_stats, monster, game_state="Combat")
