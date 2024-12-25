import random

age = 20
majeur = True if age >= 18 else False  # ternaire un peu lourde en python

# and conditions
if age >= 18 and majeur == True:
    print("majeur")

if age >= 18 or majeur == True:
    print("majeur mais en or")

# le "!" => not en python
# not True => False
test = True if "aaa".__len__() == 3 else False
print(not test)

r = random.randint(0, 2)
print(r)

r2 = random.uniform(0, 2)
print(r2)

r3 = random.randrange(999) # ici de 0 a 998 - param exclusif
