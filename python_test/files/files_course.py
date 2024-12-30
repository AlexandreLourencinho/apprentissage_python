from constants_utils.constants import Constants as const

path = "c:/Users/alexandre.lourencinh/dev/oc-courses/python/python_test/files/fichier_1.txt"
path_save = "c:/Users/alexandre.lourencinh/dev/oc-courses/python/python_test/files/fichier_1_save.txt"

f = open(path, "r")
print(f)
print(f.read()) #ok
print(f.read()) #empty
f.seek(0)
print("réinit")
print(f.read())
f.seek(10) # cursor pos 10th char
print(f.read())
f.seek(0)
print(f.read(10)) # read 10 first characters
f.close()

def red_file():
    global ff, content
    with open(path, "r", encoding="utf-8") as ff:
        print(const.SEPARATOR)
        print("met tout dans un tableau, séparé par les retours à la ligne")
        print(const.SEPARATOR)
        content = ff.read().splitlines()
        print(content)


# windows specific - sight - encoding=utf-8

# ouverture classique
with open(path, "r", encoding="utf-8") as ff:
    print(const.SEPARATOR)
    print("ouverture classique")
    print(const.SEPARATOR)
    content = ff.read()
    print(content)

# pas d'interprétation des \n ici - ne marche pas avec la tabulation
with open(path, "r", encoding="utf-8") as ff:
    print(const.SEPARATOR)
    print("ouverture avec la non interprétation des retours à la ligne")
    print(const.SEPARATOR)
    content = repr(ff.read())
    print(content)

# n'interprête pas les retours à la ligne
with open(path, "r", encoding="utf-8") as ff:
    print(const.SEPARATOR)
    print("pareil qu'au dessus mais avec une syntaxe différente")
    print(const.SEPARATOR)
    content = ff.readline()
    print(content)

# séparation par retour à la ligne / par ligne en tableau
red_file()

# writing in file

# overwrite the file
with open(path, "w", encoding="utf-8") as ff:
    print(const.SEPARATOR)
    print("overwriting file")
    ff.write("bonjour")

with open(path_save, "r", encoding="UTF-8") as save_file:
    content = save_file.read().splitlines()
    print(content)
    restored = open(path, "a", encoding="UTF-8")
    for el in content:
        restored.write(el)

red_file()

# append the file
with open(path, "a", encoding="utf-8") as ff:
    print(const.SEPARATOR)
    print("append without breakline")
    ff.write("bonjour")

with open(path_save, "r", encoding="UTF-8") as save_file:
    content = save_file.read().splitlines()
    print(content)
    restored = open(path, "a", encoding="UTF-8")
    for el in content:
        restored.write(el)

red_file()

# append with breakline
with open(path, "a", encoding="utf-8") as ff:
    print(const.SEPARATOR)
    print("append with breakline")
    ff.write("\nbonjour")

with open(path_save, "r", encoding="UTF-8") as save_file:
    content = save_file.read().splitlines()
    print(content)
    restored = open(path, "w", encoding="UTF-8")
    for el in content:
        restored.write(el)

red_file()