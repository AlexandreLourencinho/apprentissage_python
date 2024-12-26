first_list = []

first_list.append(4)
print(first_list)
first_list.append(5)
first_list.remove(5)

print(first_list)

first_list.append(5)
first_list.append(5)
first_list.remove(5)
print(first_list)
# indices : 0 1 2... mais aussi de la fin ! -1 -2 ....(-1 = le dernier)
print(first_list[1])  # should be 5
print(first_list[-1])  # should also be 5
print(first_list[0])  # should be 4
print(first_list[-2])  # also 4

list_1 = ['a01',
          'a02',
          'a03',
          'a04',
          'a05',
          'a06',
          'a04']
print(list_1[0])
# slice
print(list_1[0:1])  # premier élément uniquement
print(list_1[0:2])  # deux premiers élément uniquement
print(list_1[:])  # toute la liste
print(list_1[:-1])  # jusqu'a a06 EXCLUSIF (donc non inclus)
print(list_1[2:])  # index 2 jusqu'a la fin de la liste
print(list_1[::2])  # 1 sur deux, deuxième ":" => le pas
print(list_1[1::2])  # 1 sur deux (en partant de l'index 1)
print(list_1[0:-2:2])  # 1 sur deux du début a -2
print(list_1[::-1])  # inverse l'ordre, toute la liste

resultat = list_1.index("a04")
resultat2 = list_1.count("a04")
print(resultat)
print(resultat2)
list_1.sort()  # return none
print(list_1)
list_1.reverse()  # inversion de l'ordre
print(list_1)
sorted_list = sorted(list_1)
print(sorted_list)
list_1.sort()

element = list_1.pop(-1)  # pop prend un param index
print(list_1)
print(element)
save_list = list_1.copy()  # créée une copie de la liste au lieu d'assigner la variable a la même allocation mémoire (vidant les deux listes)
list_1.clear()
print(list_1)
print(save_list)

# join - python est anglais?
join_result = "\n".join(save_list)
print(join_result)

str_to_split = "bonjour je suis une tomate"
split_result = str_to_split.split()  # vide => " " (espace)
print(split_result)

# opérateurs d'appartenance

print("a00" in save_list)
print("a01" in save_list)
print("a00" not in save_list)
print("a01" not in save_list)
