All_items = {
    "Frostmourne": {
        "Type": "Weapon",
        "Weapon Type": "Sword",
        "Attack Damage": 50,
        "Special Trigger": "20% chance to freeze the enemy for 2 turn",
        "Duration": 2
    },
    "AK-47": {
        "Type": "Weapon",
        "Weapon Type": "Gun",
        "Attack Damage": 35,  # per shot
        "Special Cast": "Rapid fire, shoots bullets rapidly dealing 90 damage, but using up 15 ammo",
        "Ammo Capacity": 30,
        "Cooldown": 3,  # Assuming cooldown, adjust as needed
        "Ammo Needed": 15,
        "Note": "Requires ammo to use"
    },
    "Ashbringer": {
        "Type": "Weapon",
        "Weapon Type": "Sword",
        "Attack Damage": 45,
        "Special Trigger": "15% chance to deal double damage"
    },
    "Skeleton Shield": {
        "Type": "Weapon",
        "Weapon Type": "Shield",
        "Defence": 25,
        "Special Trigger": "10% chance to reflect 25% of the damage back to the attacker"
    },
    "Wooden Shield": {
        "Type": "Weapon",
        "Weapon Type": "Shield",
        "Defence": 15,
        "Durability": "Moderate (can break after extensive use)"
    },
    "Pillow": {
        "Type": "Weapon",
        "Weapon Type": "Defence Item",
        "Defence": 5,
        "Note": "Mostly for fun, low practical use",
        "Special Trigger": "When hit there's a 10% chance of reducing incoming damage by 25%"
    },
    "Book": {
        "Type": "Weapon",
        "Weapon Type": "Misc",
        "Attack Damage": 10,  # when thrown
        "Special Cast": "Can contain clues or spells",
        "Cooldown": 4
    },
    "Rock": {
        "Type": "Weapon",
        "Weapon Type": "Thrown",
        "Attack Damage": 15
    },
    "Crossbow of Silence": {
        "Type": "Weapon",
        "Weapon Type": "Crossbow",
        "Attack Damage": 30,
        "Special Cast": "Silences the enemy for 2 turns, preventing them from using special abilities",
        "Cooldown": 5,
        "Duration": 2
    },
    "Mystic Wand": {
        "Type": "Weapon",
        "Weapon Type": "Wand",
        "Attack Damage": 20,
        "Special Trigger Ability": "25% chance to cast a random spell (e.g., fireball, healing, stun)"
    },
    "Thunder Hammer": {
        "Type": "Weapon",
        "Weapon Type": "Hammer",
        "Attack Damage": 40,
        "Special Trigger Ability": "15% chance to summon a thunder strike, dealing extra 20 damage"
    },
    "Dual Daggers": {
        "Type": "Weapon",
        "Weapon Type": "Dagger",
        "Attack Damage": 25,  # Combined
        "Special Trigger": "Grants an extra attack every third turn"
    },
    "Banana Peel": {
        "Type": "Weapon",
        "Weapon Type": "Whacky",
        "Attack Damage": 5,
        "Special Trigger": "50% chance to make the enemy slip, causing them to lose a turn",
        "Duration": 1
    },
    "Rubber Chicken": {
        "Type": "Weapon",
        "Weapon Type": "Whacky",
        "Attack Damage": 10,
        "Special Cast": "Can be used to distract enemies, increasing your dodge chance by 30% for 2 turn",
        "Duration": 2,
        "Cooldown": 4
    },
    "Spaghetti Whip": {
        "Type": "Weapon",
        "Weapon Type": "Whacky",
        "Attack Damage": 15,
        "Special Trigger": "20% chance to entangle the enemy, reducing their attack damage by 10 for 3 turns",
        "Duration": 3
    },
    "Magic Yo-Yo": {
        "Type": "Weapon",
        "Weapon Type": "Whacky",
        "Attack Damage": 20,
        "Special Trigger": "30% chance to return to the player after an attack, allowing for an immediate second strike"
    },
    "Bubble Blower": {
        "Type": "Weapon",
        "Weapon Type": "Whacky",
        "Attack Damage": 12,
        "Special Cast": "Blows bubbles that have a 25% chance to trap the enemy for 4 turns",
        "Duration": 4,
        "Cooldown": 4
    },
    "Squeaky Hammer": {
        "Type": "Weapon",
        "Weapon Type": "Whacky",
        "Attack Damage": 18,
        "Special Trigger": "Makes a squeaking sound"
    },
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
    "Blanket": {
        "Type": "Misc",
        "Defence": 5,
        "Dodge": 10,
        "Special Cast": "Can be used for stealth or disguise, turns you invisible for 2 rounds",
        "Cooldown": 5
    },
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
    "Potion of Small Health": {
        "Type": "Health Potion",
        "Health Boost": 5,
        "Duration": 0
    },
    "Potion of Medium Health": {
        "Type": "Health Potion",
        "Health Boost": 10,
        "Duration": 0
    },
    "Potion of Large Health": {
        "Type": "Health Potion",
        "Health Boost": 20,
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
        "Effect": "Uknown"

    },
    "Potion of Fortitude": {
        "Type": "Potion",
        "Effect": "Increase Defence (potion)",
        "Defence": 20,  # Defence boost
        "Duration": 3   # Turns
    },

    "Potion of Vulnerability": {
        "Type": "Potion",
        "Effect": "Decreases Defence (potion)",
        "Defence": -20,  # Defence reduction
        "Duration": 3   # Turns
    },

    "Potion of Agility": {
        "Type": "Potion",
        "Effect": "Increases Dodge (potion)",
        "Dodge": 15,   # Dodge boost (converted from percentage)
        "Duration": 3  # Turns
    },

    "Potion of Clumsiness": {
        "Type": "Potion",
        "Effect": "Decreases Dodge (potion)",
        "Dodge": -15,  # Dodge reduction (converted from percentage)
        "Duration": 3  # Turns
    }

}
