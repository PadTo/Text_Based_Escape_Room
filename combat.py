from text_effect import *
from monsters import *
import random
from inventory import *
from effects import *
import monsters

global game_state


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
        damage = calculate_damage(attacker["Attack"], defender["Defence"])
        defender["Health"] -= damage
        attacker_name = attacker["Name"]
        deffender_name = defender["Name"]
        type_effect(f"{attacker_name} attacks for {damage} damage!")
        type_effect(f"{deffender_name} Health: {defender['Health']}")


def player_action(player, monster, player_turn, game_state):
    cond = True
    if user_on_going_effects["Frozen"]["Duration"] > 0 or user_on_going_effects["Stunned"]["Duration"] > 0:
        type_effect("You are stunned.")
        return
    else:
        while cond:
            action = input(
                "Choose action: Attack (a), Use Ability (u), Switch Weapons (s), Drink Potion (p), Run Away (r): ").lower()
            if action == 'a':
                combat_round(player, monster, player_turn)
                cond = False
            elif action == 'u':

                if check_if_equiped_item_abilities_true():
                    cond = False
                else:
                    pass
            elif action == "s":
                if check_if_equiped_item_abilities_true():
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

    while player["Health"] > 0 and monster["Health"] > 0:

        if player_turn:
            turn_tracker += 1
            player_action(player, monster, player_turn, game_state)
            user_effects_timer()
        else:
            if monster_on_going_effects["Frozen"]["Duration"] > 0 or monster_on_going_effects["Stunned"]["Duration"] > 0:

                pass
            else:
                combat_round(monster, player, player_turn)
                monster_effects_timer()

        if game_state != "Combat":
            type_effect("You have run away, coward...")
            game_state = "Exploration"
            break

        player_turn = not player_turn

    if player["Health"] > 0:
        # Add double loot here #
        type_effect("You have defeated the enemy, congratulations!")
        game_state = "Exploration"
    else:
        type_effect("You have died...")
        game_state = "Dead"


# monster = bosses["Lich King"]
# combat(character_stats, monster)
