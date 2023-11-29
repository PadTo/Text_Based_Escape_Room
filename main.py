import random as rand
import numpy as np


from text_effect import type_effect
from items import *
from inventory import *
from abilities import *
from combat import *
from constants import *

add_item_to_inventory("Potion of Small Health", 1)
use_potion("Potion of Small Health")
character_stats_display()
