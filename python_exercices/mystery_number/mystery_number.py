import random
from constant_classes.yes_no_constants import YesNoConstants as yn_const

# goal ici : nbre entre 1 et 100, choisir un mode (facile / moyen / dur) et deviner le nombre généré aléatoirement
# que des entiers
# facile = 10 tentatives, moyen = 7, dur = 5 ?
# à voir si pas presque impossible a trois
# garder le principe du plus petit plus grand évidemment

play = 1

while play == 1:
    the_number = random.randint(1, 100)

    print("bonjour ! vous allez devoir deviner le nombre mystère!")
    print("pour celà, vous devrez entrer un nombre, et nous vous dirons si le nombre mystère est")
    print("plus petit ou plus grand que votre nombre.")
    print("vous aurez un nombre de tentatives différent selon la difficulté que vous choisirez.")
    difficulty = input(
        "choisissez votre difficulté : 1- Facile(10 tentatives), 2- Moyen(8 tentatives) ou 3- Difficile(5 tentatives)\n")

    while True:
        try:
            difficulty = int(difficulty)
            attempts = 0
            if difficulty == 1:
                attempts = 10
                break
            elif difficulty == 2:
                attempts = 8
                break
            elif difficulty == 3:
                attempts = 5
                break
            else:
                print("la difficulté doit être 1 (facile),2(moyen) ou 3(difficile).")

        except ValueError:
            print("veuillez entrer 1, 2 ou 3 pour choisir la difficulé!")
            difficulty = input("veuillez entrer 1(facile), 2(moyen) ou 3(difficile) pour choisir la difficulé!\n")

    i = attempts
    while i > 0:
        print(f"tentatives restantes : {i}")
        guess = input("entrez votre nombre! tentez de deviner le nombre mystère!\n")

        try:
            guess = int(guess)
        except ValueError:
            print("entrez un nombre! paf une tentative de moins pour la peine!")
            i -= 1
            continue

        if guess > 100:
            print("le nombre est compris entre 1 et 100...")
            i -= 1
        elif guess == the_number:
            print("vous avez trouvé le numéro mystère! bravo!")
            print(f"le numéro mystère était {the_number}")
            print("félicitation!")
            break
        elif guess > the_number:
            print("plus petit!")
            i -= 1
        else:
            print("plus grand!")
            i -= 1

    if guess != the_number:
        print("Perdu! vous n'avez pas trouvé le nombre mystère!")
        print(f"le nombre mystère était : {the_number}")

    user_retry = ""

    while user_retry.lower() not in yn_const.NO_ARRAY and user_retry.lower() not in yn_const.YES_ARRAY:

        user_retry = input("voulez-vous retenter une partie? Oui/Non\n")
        if user_retry.lower() in yn_const.NO_ARRAY:
            print("d'accord, merci d'avoir joué!")
            play = 0
        elif user_retry.lower() in yn_const.YES_ARRAY:
            print("très bien, jouons encore!")
        else:
            print("euh, il faut répondre oui ou non !")
