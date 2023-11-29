import random as rand
import numpy as np


from text_effect import type_effect
from items import *
from inventory import *
from abilities import *
from combat import *
from constants import *

# Example of adding an item


add_item_to_inventory("Frostmourne", 1)

# Example of removing an item
# add_item_to_inventory("Potion of Dodge Chance", 1)
# remove_item_from_inventory("Frostmourne", 1)
# display_inventory()

equip("Frostmourne")

# gear()
# item_stats("Frostmourne")
character_stats_display()
