from text_effect import *
from monsters import *
import random
from inventory import *
from effects import *
from abilities import trigger_weapon_shield_ability


global game_state


def calculate_damage(attack, defence):
    damage = attack - (defence // 2)
    return max(damage, 0)


def combat_round(attacker, defender, player_turn):
    chance = random.random()

    if defender["Dodge"]/100 > chance and not player_turn:
        type_effect("You have evaded an attack!!")
        print()
    elif defender["Dodge"]/100 > chance and player_turn:
        type_effect("You have missed...")
        print()
    else:
        if player_turn:
            trigger_weapon_shield_ability(defender, type=0)
            damage = calculate_damage(attacker["Attack"], defender["Defence"])
            defender["Health"] -= damage
            attacker_name = attacker["Name"]
            deffender_name = defender["Name"]
            type_effect(f"{attacker_name} attacks for {damage} damage!")
            type_effect(f"{deffender_name} Health: {defender['Health']}")
            print()
        elif not player_turn:
            if equiped_gear["Shield"] is not None:

                if "Special Trigger" in All_items[equiped_gear["Shield"]]:
                    damage = calculate_damage(
                        attacker["Attack"], defender["Defence"])
                    new_damage = trigger_weapon_shield_ability(
                        attacker, type=1, damage=damage)
                    # print(new_damage)
                    attacker_name = attacker["Name"]
                    deffender_name = defender["Name"]

                    if attacker["Health"] > 0:
                        type_effect(
                            f"{attacker_name} attacks for {new_damage} damage!")
                        defender["Health"] -= new_damage
                        type_effect(
                            f"{deffender_name} Health: {defender['Health']}")
                        print()
                    else:
                        do_nothing = []

                else:
                    pass
            else:
                damage = calculate_damage(
                    attacker["Attack"], defender["Defence"])
                defender["Health"] -= damage
                attacker_name = attacker["Name"]
                deffender_name = defender["Name"]
                type_effect(f"{attacker_name} attacks for {damage} damage!")
                type_effect(f"{deffender_name} Health: {defender['Health']}")
                print()


def player_action(player, monster, player_turn, game_state):
    cond = True
    if user_on_going_effects["Frozen"]["Duration"] > 0 or user_on_going_effects["Stunned"]["Duration"] > 0:
        type_effect("You are stunned.")
        return
    else:
        while cond:
            action = input(
                "Choose action: Attack (a), Use Ability (u), Switch Weapons (s), Drink Potion (p), Run Away (r): ").lower()
            print()
            if action == 'a':
                combat_round(player, monster, player_turn)
                cond = False
            elif action == 'u':

                if check_if_equiped_item_abilities_true():
                    cond = False
                else:
                    pass
            elif action == "s":
                if check_if_weapons_or_shields_true():
                    cond = False
                else:
                    pass

            elif action == "d":
                if check_if_weapons_or_shields_true():
                    cond = False
                else:
                    pass
            elif action == 'p':
                if check_if_potions_true(game_state):
                    cond = False
                else:
                    pass

            elif action == 'r' and monster["Type"] != "Boss":
                game_state = "Exploration"
                return game_state

            elif action == 'r' and monster["Type"] == "Boss":
                type_effect(f"You can't run away from the {monster['Name']}")
                pass

            else:
                type_effect("Invalid action.")


def combat(player, monster, game_state="Combat"):
    player_turn = True
    turn_tracker = 0
    type_effect(f"You just entered combat with the {monster['Name']}!!")
    from character import character_stats
    stats_before_combat = character_stats_before_combat(character_stats)

    while player["Health"] > 0 and monster["Health"] > 0:

        if player_turn:
            turn_tracker += 1

            if cant_move(0):
                do_nothing = []
                monster_effects_timer()
            else:
                player_action(player, monster, player_turn, game_state)
                monster_effects_timer()
        else:
            if cant_move(1):
                user_effects_timer()
                do_nothing = []
            else:
                combat_round(monster, player, player_turn)
                if monster["Health"] < 0:
                    break

                user_effects_timer()

        if game_state != "Combat":
            type_effect("You have run away, coward...")
            game_state = "Exploration"
            break

        player_turn = not player_turn

    if player["Health"] > 0:
        type_effect("You have defeated the enemy, congratulations!")
        game_state = "Exploration"
        current_health = health_after_combat()
        character_stats = stats_before_combat
        character_stats["Health"] = current_health
        game_state = "Exploration"

    else:
        type_effect("You have died...")
        game_state = "Dead"
