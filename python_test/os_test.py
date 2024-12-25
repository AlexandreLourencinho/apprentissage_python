import os
from pprint import pprint

chemin = "/Users/alexandre.lourencinh/dev/oc-courses/python/python_test"
chemin = os.path.join(chemin, "dossier")

print(chemin)
if not os.path.exists(chemin):
    os.makedirs(chemin)

if os.path.exists(chemin):
    os.removedirs(chemin)

os.makedirs(chemin, exist_ok = True)

print(dir(os))
help(os.makedirs)
pprint(dir(os))

print(callable(pprint))
print(callable(os))
print(callable(os.name))
print(os.name)