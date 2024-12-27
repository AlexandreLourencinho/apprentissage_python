import time
import random

num_list = [0, 3, 5, 6, 9, 45, 10]
str_stub = "I am here"

for i in num_list:
    print(i)

for letter in str_stub:
    print(letter)

for i in range(100):
    print(f"hello for the {i} time" + (
        "s" if i > 1 else "") + "!")  # pretty sure there's never a S here but wtv ... just for the algo

rand_num = random.randint(0, 50)

i = 0
while i < rand_num:
    print("on y est encore!")
    i += 1

i = 0

while i < rand_num:
    print("ça sleep ici !")
    time.sleep(1)
    i += 1

for i in range(0, rand_num):
    if i % 2 == 0:
        continue
    else:
        print(i)

for i in range(0, rand_num):
    if i % 2 != 0:
        print(i)
        print(i / 2)
        break
    else:
        continue

# for else : execute le else si pas de break dans la boucle
for i in num_list:
    if i == 51:
        print("impossiburu!")
        break
else:
    print("oh bah y'a pas de pastis!")

m_list = [-6, -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 6]
r_list = [i for i in m_list]
print(r_list)
r_list = [i for i in m_list if i > 0]
print(r_list)
r_list = [i * 2 for i in m_list]
print(r_list)
r_list = [i * 3 for i in m_list if i < 0]
print(r_list)
print(all([ i > 0 for i in m_list]))
print(any([ i > 0 for i in m_list]))
