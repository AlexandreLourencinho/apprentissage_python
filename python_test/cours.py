import math
from constants import TEST, test

nombre = 5
nombre2 = nombre
print(id(nombre))
print(id(nombre2))
id(500)
print(nombre2)

a, b = 10, 12
print(a)
print(b)
print(id(True))
print(id(True))

# variable plutot avec des _ que du camelCase
# test = input("input test")
# print(test)
# str.strip() +- trim() (si pas de paramètres)
# les paramètres n'ont pas besoin d'ordre pour strip, les caractères sont tous pris en compte individuellement
# exemple : " Bonjour 3.strip(" ujor") => "bon"
# strip => rstrip et lstrip (right et left)
# str.split()
# nbre = "1, 2, 3, 4, 5, 6"
# nbre.split(", ")
# ['1', '2', '3', '4', '5', '6']
# nbre_res = nbre.split(", ")
# nbre_res
# ['1', '2', '3', '4', '5', '6']
# nbre_test = ", ".join(nbre_res)
# nbre_test
# '1, 2, 3, 4, 5, 6'

for i in range(101):
    print(str(i).zfill(
        2))  # rajoute des 0 pour remplir l'espace demandé - n'a pas d'effet si la chaine déjà de la taille précisée

print("bonjour".islower())  # true
print("Bonjour".islower())  # false
print("coucou les amis".istitle())  # false
print("Coucou Les Amis".istitle())  # true
print("50".isdigit())  # true
print("a".isdigit())  # false
print("50a".isdigit())  # false
print("bonjour le jour".count("jour"))  # => 2

test = input("nombre :\n")
if test.isdigit():
    print("c'est un nombre t'as de la chance")
else:
    print("traître!")

test_count = input("tape un truc : \n")
result = test_count.count("e")
print("y'a " + str(result) + " e dans ta chaîne")

print("bonjour le jour".index("jour"))  # => 3
print("bonjour le jour".find("jour"))  # => 3
print("bonjour le jour".find("soir"))  # => -1
# print("bonjour le jour".index("soir")) # => erreur (a commenter)
# existe aussi rfind() (pas lfind, puisque c'est par défaut)
print("toto.tutu".endswith("tutu"))  # => true
print("toto.tutu".endswith("prprpr"))  # => false
print("toto.tutu".startswith("prprpr"))  # => false
print("toto.tutu".startswith("toto"))  # => true

test_list = '"a", "z", "k", "y", "iezrhge"'
print(test_list.replace("\"", ""))
print(test_list.replace("\"", "").split(", "))
res_list = test_list.replace("\"", "").split(", ")
res_list.sort()
print(res_list)
print(", ".join(res_list))

print("test" * 3)
print(6 / 2)  # => float !!
print(6 // 2)  # => division entière
print(10 / 3)
print(10 // 3)
print(2 ** 4)  # puissance / exponentielle (16)
print(math.pow(2, 4))  # puissance / exponentielle (16)
print(math.exp(2))  # e^x (math.exp(2) => e^2
print(math.sqrt(16)) # => square root (4)

print(math.ceil(-4.8)) # => entier immédiatement SUPERIEUR => -4
print(math.floor(-4.8)) # => entier immédiatement inférieur => -5
print(math.ceil(-4.2)) # => -4
print(math.floor(-4.2)) # => -5
i = 0
print(i)
i += 1
print(i)

print("1" == "1")
print(1 > 2)
print(1 != 2)

a = "kroeglerngl"
b = a
print (a is b)
print(b == a)
print(b == "zfefef")
print(b is "zfefef")
print (a is "kroeglerngl") # => attention is est pour la comparaison pour le même objet (même allocation mémoire - voir id())
t = "bien le bonjour c'est moi qui fait du python et je ne sais pas quoi écrire ici "
y = "bien le bonjour c'est moi qui fait du python et je ne sais pas quoi écrire ici "
print(id(y))
print(id(t))
print(t is y)
print (t == y)
test_f_string = "toutoutiti"
print(f"le mot fstring est : {test_f_string}") # +- = a js : ` test 1 ${variable}`
#pre python 3.6
age = 34
print("j'ai {age} ans.".format(age=age))
print("j'ai {} ans.".format(age))
print("j'ai {} ans., je m'appelle {}".format(age, "Alexandre"))
print("j'ai {0} ans, {0} ans".format(age))
print("j'ai {1} ans, {0} ans".format(age, 56))
print("j'ai {toto} ans.".format(toto=age))
# marche avec des indices, des noms de variable, ou par ordre des paramètres

print(TEST.format("je suis le paramètre."))