import random as rand
import numpy as np


from text_effect import type_effect
from inventory import add_item_to_inventory as add
from inventory import remove_item_from_inventory as remove
from inventory import display_inventory as inventory

# Example of adding an item
add('Sword', 1)

# Example of removing an item
remove('Potion', 1)

inventory()
