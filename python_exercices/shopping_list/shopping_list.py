from colors import bcolors

# goal is to manage a shopping list (without db or file save for now)

shopping_list = []
print(bcolors.HEADER + "gérons notre liste de course!")

while True:
    print(bcolors.ENDC + "pour l'instant, votre liste contient:")
    print(shopping_list)
    user_input = input(bcolors.WARNING + "voulez vous gérer votre liste de course? N/O\n")

    if user_input.lower() == "n" or user_input.lower() == "non" or user_input.lower() == "no":
        print(bcolors.OKCYAN + "très bien, au revoir! voici votre liste :")
        print(shopping_list)
        break

    elif user_input.lower() == "o" or user_input.lower() == "y" or user_input.lower() == "oui" or user_input.lower() == "yes":
        user_choice = ""

        while user_choice != "0":
            print(bcolors.ENDC + "très bien! que voulez vous faire?" if user_choice == "" else "Que voulez-vous faire?")
            print(bcolors.OKBLUE + "1- ajouter un élément dans la liste")
            print("2- supprimer un élément de la liste")
            print("0- arrêter de gérer la liste")
            print(bcolors.ENDC + "pour rappel, voici votre liste actuelle :")
            print(shopping_list)
            user_choice = input()

            if user_choice == "1":
                print(bcolors.UNDERLINE + "rappel : les majuscules/minuscules et accents sont importants!")
                user_add = input(bcolors.ENDC + "tapez l'élément que vous voulez rajouter dans votre liste de course :\n")
                shopping_list.append(user_add)
                print(bcolors.OKGREEN + f"vous avez bien ajouté '{user_add}' à votre liste.")

            elif user_choice == "2":
                to_delete = input(bcolors.ENDC + "Tapez le nom de ce que vous voulez retirer de votre liste: \n")
                try:
                    shopping_list.remove(to_delete)
                    print(bcolors.UNDERLINE + f"très bien! '{to_delete}' a bien été supprimé de votre liste.")
                    print(bcolors.ENDC + "voici votre liste de courses mise à jour :")
                    print(shopping_list)
                except ValueError:
                    print(bcolors.FAIL + "Ce que vous avez tapez n'existe pas dans la liste!")
                    print(bcolors.ENDC + "voici votre liste, pour rappel:")
                    print(shopping_list)

            elif user_choice == "0":
                print(bcolors.ENDC + "très bien, retournons à l'étape précédente!")

            else:
                print(bcolors.FAIL + "désolé, votre commande n'a pas été reconnue.")
                print(bcolors.WARNING + "pour rappel, utilisez 1 pour ajouter un élément dans votre liste, 2 pour en enlever un.")


    else:
        print(bcolors.FAIL + "Votre commande n'est pas gérée par ce programme !")
        print(bcolors.UNDERLINE + "rappel: si vous voulez arrêter de gérer votre liste, appuyez sur N.")
        print(bcolors.UNDERLINE + "Si vous voulez la modifier, au contraire, appuyez sur la lettre O.")
