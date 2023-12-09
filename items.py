All_items = {

    "Frostmourne": {
        "Type": "Weapon",
        "Weapon Type": "Sword",
        "Attack Damage": 50,
        "Ability Name": "Freeze",
        "Special Trigger": "20% chance to freeze the enemy for 2 turns",
        "Duration": 2,
        "Trigger Chance": 100  # in percent
    },

    "Ashbringer": {
        "Type": "Weapon",
        "Weapon Type": "Sword",
        "Attack Damage": 45,
        "Ability Name": "Double Damage",
        "Multiplier": 2,
        "Special Trigger": "15% chance to deal double damage",
        "Duration": 1,
        "Trigger Chance": 100
    },
    "Skeleton Shield": {
        "Type": "Weapon",
        "Weapon Type": "Shield",
        "Defence": 25,
        "Ability Name": "Reflect Damage",
        "Special Trigger": "10% chance to reflect 25% of the damage back to the attacker",
        "Trigger Chance": 100,
        "Damage Reduction": 25
    },
    "Wooden Shield": {
        "Type": "Weapon",
        "Weapon Type": "Shield",
        "Defence": 15,
        "Durability": "Moderate (can break after extensive use)",
        "Trigger Chance": None  # No special ability
    },
    "Pillow": {
        "Type": "Weapon",
        "Weapon Type": "Shield",
        "Defence": 5,
        "Note": "Mostly for fun, low practical use",
        "Ability Name": "Soft Block",
        "Special Trigger": "When hit there's a 30% chance of reducing incoming damage by 25%",
        "Trigger Chance": 100,
        "Damage Reduction": 25  # Percentage
    },

    "Rock": {
        "Type": "Weapon",
        "Weapon Type": "Thrown",
        "Attack Damage": 15,
        "Trigger Chance": None  # No special ability
    },
    "Crossbow of Silence": {
        "Type": "Weapon",
        "Weapon Type": "Crossbow",
        "Attack Damage": 30,
        "Ability Name": "Silence",
        "Special Cast": "Silences the enemy for 3 turns, preventing them from using special abilities",
        "Cooldown": 5,
        "Duration": 3,
        "Trigger Chance": None  # Special cast, not a random trigger
    },
    "Mystic Wand": {
        "Type": "Weapon",
        "Weapon Type": "Wand",
        "Attack Damage": 20,
        "Ability Name": "Random Spell",
        "Special Trigger": "25% chance to cast a random spell (e.g., fireball, healing, stun)",
        "Trigger Chance": 100
    },
    "Thunder Hammer": {
        "Type": "Weapon",
        "Weapon Type": "Hammer",
        "Attack Damage": 40,
        "Ability Name": "Thunder Strike",
        "Special Trigger": "15% chance to summon a thunder strike, dealing extra 70 damage",
        "Trigger Chance": 100,
        "Extra Damage": 70
    },


    "Banana Peel": {
        "Type": "Weapon",
        "Weapon Type": "Whacky",
        "Attack Damage": 5,
        "Ability Name": "Slip",
        "Special Trigger": "50% chance to make the enemy slip, causing them to lose 2 turns",
        "Duration": 2,
        "Trigger Chance": 100
    },

    "Spaghetti Whip": {
        "Type": "Weapon",
        "Weapon Type": "Whacky",
        "Attack Damage": 15,
        "Ability Name": "Entangle",
        "Special Trigger": "20% chance to entangle the enemy, reducing their attack damage by 10 for 3 turns",
        "Duration": 3,
        "Trigger Chance": 100
    },
    "Magic Yo-Yo": {
        "Type": "Weapon",
        "Weapon Type": "Whacky",
        "Attack Damage": 20,
        "Ability Name": "Return Strike",
        "Special Trigger": "30% chance to return to the player after an attack, allowing for an immediate second strike",
        "Trigger Chance": 100
    },
    "Bubble Blower": {
        "Type": "Weapon",
        "Weapon Type": "Whacky",
        "Attack Damage": 12,
        "Ability Name": "Trap",
        "Special Cast": "Blows bubbles that have a 40% chance to trap the enemy for 4 turns",
        "Duration": 4,
        "Cooldown": 4,
        "Trigger Chance": 100
    },
    "Squeaky Hammer": {
        "Type": "Weapon",
        "Weapon Type": "Whacky",
        "Attack Damage": 30,
        "Special Trigger": "Makes a squeaking sound",
        "Trigger Chance": 100  # More for fun, no combat effect
    },


    # Helmets
    "Iron Helm": {
        "Type": "Helm",
        "Defence": 15,
    },
    "Leather Cap": {
        "Type": "Helm",
        "Defence": 10,
        "Dodge": 5
    },
    "Steel Helm": {
        "Type": "Helm",
        "Defence": 20,
    },
    # Body Armor
    "Chainmail": {
        "Type": "Body Armor",
        "Defence": 30,
    },
    "Leather Armor": {
        "Type": "Body Armor",
        "Defence": 20,
    },
    "Plate Armor": {
        "Type": "Body Armor",
        "Defence": 40,
    },
    # Miscellaneous
    "Blanket": {
        "Type": "Misc",
        "Defence": 5,
        "Dodge": 10,
        "Ability Name": "Stealth",
        "Special Cast": "Can be used for stealth or disguise, turns you invisible for 2 rounds",
        "Cooldown": 5,
        "Duration": 2
    },
    # Footwear
    "Leather Boots": {
        "Type": "Footwear",
        "Defence": 10,
    },
    "Steel-toed Boots": {
        "Type": "Footwear",
        "Defence": 15,
    },
    "Sneakers": {
        "Type": "Footwear",
        "Defence": 5,
        "Dodge": 5
    },
    # Potions
    "Potion of Small Health": {
        "Type": "Health Potion",
        "Health Boost": 30,
        "Duration": 0
    },
    "Potion of Medium Health": {
        "Type": "Health Potion",
        "Health Boost": 60,
        "Duration": 0
    },
    "Potion of Large Health": {
        "Type": "Health Potion",
        "Health Boost": 100,
        "Duration": 0
    },
    "Potion of Dodge Chance": {
        "Type": "Potion",
        "Dodge": 20,
        "Duration": 3
    },
    "Potion of Defence": {
        "Type": "Potion",
        "Defence": 15,
        "Duration": 5  # Turns,
    },
    "Potion of Greed": {
        "Type": "Potion",
        "Effect": "Doubles any loot found",
        "Defence": -10,
        "Duration": 4,
    },
    "Potion of the Unknown": {
        "Type": "Potion",
        "Duration": 3,
        "Effect": "Unknown"
    },
    "Potion of Fortitude": {
        "Type": "Potion",
        "Ability Name": "Fortitude Boost",
        "Defence": 20,  # Defence boost
        "Duration": 3   # Turns
    },
    "Potion of Vulnerability": {
        "Type": "Potion",
        "Ability Name": "Vulnerability Curse",
        "Defence": -20,  # Defence reduction
        "Duration": 3   # Turns
    },
    "Potion of Agility": {
        "Type": "Potion",
        "Ability Name": "Agility Boost",
        "Dodge": 15,   # Dodge boost (converted from percentage)
        "Duration": 3  # Turns
    },
    "Potion of Clumsiness": {
        "Type": "Potion",
        "Ability Name": "Clumsiness Curse",
        "Dodge": -15,  # Dodge reduction (converted from percentage)
        "Duration": 3  # Turns
    },
    # ... [Other items continue as they were]
}
