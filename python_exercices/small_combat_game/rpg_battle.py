import random
from constant_classes.ascii import AsciiArt as ascii
from constant_classes.colors import bcolors
import time


# ici, il s'agit de faire un combat contre un mob, avec une barre de vie pour le joueur et le mob
# le joueur a 3 potions, peu attaquer, et je vais essayer d'inclure des chances de toucher
# des chances d'esquive, et la possibilité de se défendre (dégats / 2)
# 1 = attaque, 2 = défend, 3 = potion

print(ascii.CROSSED_SWORDS)
time.sleep(3)

# mob values
hp_mob = 75
health_pot_mob = 1
mob_dodge = 5
mob_hit_chance = 85
mob_crit_chance = 5
mob_min_damage = 2
mob_max_damage = 10

# player values
hp_player = 115
health_pot_player = 3
player_dodge = 10
player_hit_chance = 95
player_crit_chance = 10

# difficulty choice
while True:
    print("choisissez la difficulté du combat!")
    print("1- facile, 2- moyen, 3- difficile!")

    try:
        difficulty = int(input())
        break
    except ValueError:
        print("vous devez choisir une difficulté!")
        print("1- facile, 2- moyen, 3- difficule!")

# difficulty management. if medium => * 1.5, hard => *2
if difficulty == 1:
    print("difficulté facile choisie!")
    time.sleep(1)
elif difficulty == 2:
    mob_min_damage = round(mob_min_damage * 1.5)
    mob_max_damage = round(mob_max_damage * 1.5)
    hp_mob = round(hp_mob * 1.5)
    print("difficulté moyenne choisie!")
    time.sleep(1)
else:
    mob_min_damage = round(mob_min_damage * 2)
    mob_max_damage = round(mob_max_damage * 2)
    hp_mob = round(hp_mob * 2)
    health_pot_mob = health_pot_mob * 2
    print("difficulté la plus élevée choisie!")
    time.sleep(1)

# The battle loop !
while hp_mob > 0 and hp_player > 0:

    # mob action choice
    action_mob = random.randint(1, 3 if health_pot_mob > 0 and hp_mob < 50 else 2)
    attack_player = 0
    attack_mob = 0

    print(ascii.MOB)
    time.sleep(1)

    # stats display
    print(f"Truc : {bcolors.FAIL} {hp_mob} {bcolors.ENDC}")
    print(f"Vous : {bcolors.OKGREEN} {hp_player} {bcolors.ENDC}")
    print(f"vous avez {bcolors.OKBLUE} {health_pot_player} potions {bcolors.ENDC}.")

    # player action choice
    while True:
        print("vous pouvez: ")
        print("1- attaquer")
        print("2- défendre")
        print("3- boire une potion")
        action_player = input("que voulez-vous faire?\n")

        try:
            action_player = int(action_player)
        except ValueError:
            action_player = ""

        # attack values management
        if action_player == 1:
            attack_player = random.randint(5, 20)
            print("vous vous préparez à porter une attaque!")
            time.sleep(1)
            break

        # defense stance
        elif action_player == 2:
            print("vous vous préparez à encaisser une attaque en levant votre bouclier!")
            time.sleep(1)
            break

        # health pot usage
        elif action_player == 3:
            if health_pot_player > 0:
                hp_player_regained = random.randint(15, 30)
                hp_player += hp_player_regained
                health_pot_player -= 1

                if hp_player > 115:
                    hp_player = 115
                    print(ascii.HEALTH_POT)
                print(
                    f"vous avez bu une potion et récupéré {bcolors.OKCYAN} {hp_player_regained} {bcolors.ENDC} points de vie !")
                print(f"vous avez désormais {bcolors.OKGREEN} {hp_player} {bcolors.ENDC} points de vie.")
                time.sleep(3)
                break

            else:
                print(f"{bcolors.WARNING} vous n'avez plus de potions! {bcolors.ENDC}")
                time.sleep(3)

        # not good input management
        else:
            print("vous devez choisir une action parmi celles proposées!")
            time.sleep(1)

    # attack management for mob
    if action_mob == 1:
        attack_mob = random.randint(mob_min_damage, mob_max_damage)
        print("truc va attaquer!")
        time.sleep(1)
    # defense stance for mob
    elif action_mob == 2:
        print("truc se prépare à encaisser le choc!")
        time.sleep(1)

    # pot management for mob
    else:
        print("truc boit une potion!")
        print(ascii.HEALTH_POT)
        time.sleep(2)
        hp_mob_gained = random.randint(5, 15)
        hp_mob += hp_mob_gained
        print(f"truc a regagné {bcolors.OKGREEN} {hp_mob_gained} {bcolors.ENDC} points de vie!")
        health_pot_mob -= 1
        time.sleep(2)

    #player attack management
    if action_player == 1:
        print("vous portez un coup d'épée à truc!")
        print(ascii.WEAPON)
        time.sleep(2)
        if player_hit_chance > random.randint(0, 100):

            #mob dodge management
            if mob_dodge > random.randint(0, 100):
                print("oh non! truc a esquivé! il ne prend aucun dégat!")
                time.sleep(2)
            # mob getting hit
            else:
                print("il le prend dans la mouille!")
                print(ascii.IMPACT)
                time.sleep(2)
                did_player_crit = random.randint(1, 100) < player_crit_chance
                final_player_damages = attack_player if action_mob != 2 else round(attack_player / 2)

                #player crit management
                if did_player_crit:
                    final_player_damages = final_player_damages * 2
                    print("vous infligez le double de dégat grâce à un coup critique!")
                    time.sleep(2)

                hp_mob -= final_player_damages

                #mob defense stance
                if action_mob == 2:
                    print("truc s'est préparé et n'a pris que la moitié des dégats.")
                    print(ascii.MOB_SHIELD)
                print(f"truc a pris {bcolors.FAIL} {final_player_damages} dégats {bcolors.ENDC}!")
                print(f"il reste {bcolors.WARNING} {hp_mob} {bcolors.ENDC} points de vie à truc.")
                time.sleep(3)

        #player misses
        else:
            print("oh non! vous l'avez loupé!")

    #mob get ko'd
    if hp_mob <= 0:
        print(f"{bcolors.WARNING} les points de vie de truc sont tombés à 0! {bcolors.WARNING}")
        break

    #mob attack management
    if action_mob == 1:
        print(ascii.MOB_WEAPON_MACE)
        print("oh non! truc essaie de vous en mettre une!")

        if mob_hit_chance > random.randint(0, 100):

            #player dodge management
            if player_dodge > random.randint(0, 100):
                print("vous avez esquivé!")
                time.sleep(1)
            #player getting it
            else:
                print("oh non, vous l'avez pris en pleine poire!")
                print(ascii.IMPACT)
                time.sleep(2)
                did_mob_crit = random.randint(1, 100) < mob_crit_chance
                final_mob_damages = attack_mob if action_player != 2 else round(attack_mob / 2)

                #mob crit management
                if did_mob_crit:
                    final_mob_damages = final_mob_damages * 2
                    print(f"{bcolors.FAIL} truc vous a mis un coup critique! ah ça pique! dégats * 2! {bcolors.ENDC}")
                hp_player -= final_mob_damages
                print(f"vous avez pris {bcolors.FAIL} {final_mob_damages} {bcolors.ENDC} dégats!")
                time.sleep(3)

                # player defense stance
                if action_player == 2:
                    print(ascii.SHIELD)
                    print(
                        f"{bcolors.OKCYAN} Vous avez encaissé le gros du choc avec votre bouclier et n'avez pris que la moitié des dégats! {bcolors.ENDC}")
                    time.sleep(3)

                print(f"il vous reste {bcolors.OKGREEN} {hp_player} {bcolors.ENDC} points de vie.")
                time.sleep(3)

        #mob misses
        else:
            print("truc vous a loupé, ouf!")
            time.sleep(1)

    #player get ko'd
    if hp_player <= 0:
        print(f" {bcolors.FAIL} vous points de vie sont tombés à 0! {bcolors.ENDC}")
        break

print("le combat est terminé!")
time.sleep(1)

# results
#draw
if hp_mob <= 0 and hp_player <= 0:
    print(f" {bcolors.WARNING} vous... vous vous êtes entre-tués! wow! {bcolors.ENDC}")
    print("ce fut un combat épique! bien joué!")

# player wins
elif hp_mob <= 0 < hp_player:
    print("vous avez battu truc!")
    print(
        f"il vous reste {bcolors.OKGREEN} {hp_player} {bcolors.ENDC} points de vie à la fin du combat ainsi que {bcolors.OKCYAN} {health_pot_player} {bcolors.ENDC} potions.")
    print("bravo pour votre victoire!")

#mob wins
elif hp_mob > 0 >= hp_player:
    print("truc vous a battu!")
    print(f"il reste à truc {bcolors.FAIL} {hp_mob} {bcolors.ENDC} point de vie.")
    print("vous gisez pitoyablement dans une mare de votre propre sang.")
    print("témor!")

# idk how to reach this one, maybe moving the above elif in an else
else:
    print("aaaargh mékoicoubeh")

#end!
print("merci d'avoir joué !")
