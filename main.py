import random as rand
import numpy as np


from text_effect import type_effect
from inventory import display_inventory as inventory
from items import *
from inventory import *
from abilities import *
from combat import *
from constants import *

# Example of adding an item


add_item_to_inventory("Frostmourne", 1)

# Example of removing an item
remove_item_from_inventory('Potion', 1)

display_inventory()

equip("Frostmourne")

gear()
