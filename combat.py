from text_effect import *
from monsters import *
import random
from inventory import *


def calculate_damage(attack, defence):
    damage = attack - (defence // 2)
    return max(damage, 0)


def combat_round(attacker, defender, player_turn):
    chance = random.random()
    if defender["Dodge"]/100 > chance and player_turn:
        type_effect("You have evaded an attack!!")
    elif defender["Dodge"]/100 > chance and not player_turn:
        type_effect("You have missed...")
    else:
        damage = calculate_damage(attacker["Attack"]), defender["Defence"]
        defender["Health"] -= damage
        type_effect(f"{attacker['Name']} attacks for {damage} damage!")


def player_action(player, monster, player_turn):
    cond = True
    while cond:
        action = input(
            "Choose action: Attack (a), Use Ability (u), Drink Potion (p), Run Away (r), Open Inventory (I): ").lower()
        if action == 'a':
            combat_round(player, monster, player_turn)
        elif action == 'u':

            pass
        elif action == 'p':
            if check_if_potions_true():
                cond = False
            else:
                pass

        elif action == 'r' and monster["Type"] != "Boss":
            return

        elif action == 'r' and monster["Type"] == "Boss":
            type_effect(f"You can't run away from the {monster['Name']}")
            pass

        else:
            type_effect("Invalid action.")


def combat(player, monster):
    player_turn = True

    while player["Health"] > 0 and monster["Health"] > 0:

        if player_turn:
            player_action(player, monster, player_turn)
        else:
            combat_round(monster, player, player_turn)

    player_turn = not player_turn

    if player["Health"] > 0:
        type_effect("You have won, congratulations!")
    else:
        type_effect("You have died...")
