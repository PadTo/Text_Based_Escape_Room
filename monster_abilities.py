def attack():
    return True

# Special ability functions (placeholders)
# Shadow Thief Abilities


def shadow_thief_shadow_step(target):
    # Teleports behind the target and strikes
    pass


def shadow_thief_disarm(player):
    # Temporarily disarms the player
    pass

# Goblin Engineer Abilities


def goblin_engineer_mechanical_fix():
    # Repairs or buffs mechanical units
    pass


def goblin_engineer_turret_deploy():
    # Deploys a stationary turret
    pass

# Mystic Sorcerer Abilities


def mystic_sorcerer_arcane_blast(target):
    # Strong magical attack against the target
    pass


def mystic_sorcerer_spell_barrier():
    # Shields from attacks
    pass

# Lich King Abilities


def lich_king_necrotic_pulse(target):
    # Area-of-effect damage
    pass


def lich_king_soul_drain(target):
    # Drains health from the player
    pass

# Fire-Breathing Dragon Abilities


def dragon_inferno_breath(target):
    # Powerful fire attack
    pass


def dragon_wing_gust(target):
    # Knocks back and damages the player
    pass


regular_enemy_abilities = {
    "Shadow Thief": {
        "basic_attack": attack,
        "shadow_step": shadow_thief_shadow_step,  # Teleports and strikes
        "disarm": shadow_thief_disarm  # Temporarily disarms the player
    },
    "Goblin Engineer": {
        "basic_attack": attack,
        "mechanical_fix": goblin_engineer_mechanical_fix,
        "turret_deploy": goblin_engineer_turret_deploy
    },
    "Mystic Sorcerer": {
        "basic_attack": attack,
        "arcane_blast": mystic_sorcerer_arcane_blast,  # Strong magical attack
        "spell_barrier": mystic_sorcerer_spell_barrier  # Shields from attacks
    },

}

boss_abilities = {
    "Lich King": {
        "basic_attack": attack,
        "necrotic_pulse": lich_king_necrotic_pulse,  # Area-of-effect damage
        "soul_drain": lich_king_soul_drain  # Drains health from the player
    },
    "Fire-Breathing Dragon": {
        "basic_attack": attack,
        "inferno_breath": dragon_inferno_breath,  # Powerful fire attack
        "wing_gust": dragon_wing_gust  # Knocks back and damages the player
    },

}
