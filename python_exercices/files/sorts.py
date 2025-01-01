from pathlib import Path
import locale

# Définit la locale en français
locale.setlocale(locale.LC_ALL, 'fr_FR.UTF-8')  # merci chatty sur ce coup là!

path = Path("c:/Users/alexandre.lourencinh/dev/oc-courses/python/python_exercices/files/name_list.txt")
output_path = path.parent / "name_list_result.txt"

with open(path, "r", encoding="utf-8") as file:
    names = file.read().strip()

print(names)

names = [name.strip() for name in
         names.split(",")]  # compréhension de liste - il faut vraiment que je me souvienne de ça

print(names)
names.sort(
    key=locale.strxfrm)  # on passe la référence à la méthode --- souviens-toi du framework de chez B auquel tu as dû passer la méthode statique !
# pour avoir la possibilité d'être utilisé et de trier les dates malgré l'impossibilité d'avoir accès aux propriétés de classes !
# si tu ne te souviens pas de quoi je parle Alexandre du futur, tu as vraiment une mauvaise mémoire

with open(output_path, "w", encoding="utf-8") as file:
    for name in names:
        file.write(name + "\n")

with open(output_path, "r", encoding="utf-8") as file:
    print(file.read())

# J'ai beaucoup trop galéré pour quelque chose d'aussi simple. Il va falloir refaire ça a froid.
