import random as rand
import numpy as np


from text_effect import type_effect
from items import *
from inventory import *
from abilities import *
from combat import *
from constants import *

add_item_to_inventory("Potion of Small Health", 1)
add_item_to_inventory("Potion of Greed", 2)
display_inventory()
use_potion("Potion of Small Health")
use_potion("Potion of Greed")
display_inventory()
character_stats_display()
inventory_space()
