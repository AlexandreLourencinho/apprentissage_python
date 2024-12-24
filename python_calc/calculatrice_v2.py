# def is_float(number):
#     if isinstance(number, float):
#         return True
#     else:
#         return False
#
#
# def is_int(number):
#     if isinstance(number, int):
#         return True
#     else:
#         return False


print("""ici, il s'agit du programme de calculatrice de base.
On va vous demander deux nombres, pour les additionner et ensuite vous afficher le résultat.
tentative version plus aboutie avec très petite base de connaissance.
tentative un poil plus aboutie.""")
nombre_1 = input("entrez le premier nombre de l'opération : \n")

try:
    nombre_1 = int(nombre_1)
except ValueError:
    try:
        nombre_1 = float(nombre_1)
    except ValueError:
        exit("votre première entrée n'est pas un nombre valide.")

operator = input("entrez l'opérateur souhaité: \n")

nombre_2 = input("entrez le second nombre de l'opération : \n")
try:
    nombre_2 = int(nombre_2)
except ValueError:
    try:
        nombre_2 = float(nombre_2)
    except ValueError:
        exit("votre entrée n'est pas un nombre valide.")

match operator:
    case "+":
        print(f"le résultat est {nombre_1 + nombre_2}")
    case "-":
        print(f"le résultat est {nombre_1 - nombre_2}")
    case "/":
        if nombre_2 == 0 or nombre_2 == 0.0:
            print("on ne divise pas par 0! sauvage! barbare!")
            exit("intolérable!")
        else:
            print(f"le résultat est {nombre_1 / nombre_2}")
    case "*":
        print(f"le résultat est {nombre_1 * nombre_2}")
    case _:
        print("l'opérateur n'existe pas .")
