import json
from pathlib import Path
import shutil

path = "c:/Users/alexandre.lourencinh/dev/oc-courses/python/python_test/files/my_json.json"
path2 = Path(path)
print(path2)
print(path2.anchor)
print(path2.name)
print(path2.drive)
print(path2.parents)
print(path2.parent)
print(path2.suffix)
print(path2.parts)
print(path2.root)
print(path2.suffixes)
print(path2.stem)

with open(path, "w", encoding="utf-8") as f:
    json.dump("Bonjour", f)

with open(path, "r", encoding="utf-8") as f:
    json_result = json.load(f)
    print(json_result)

with open(path, "w", encoding="utf-8") as f:
    json.dump(list(range(10)), f)

with open(path, "r", encoding="utf-8") as f:
    json_result = json.load(f)
    print(json_result)

with open(path, "w", encoding="utf-8") as f:
    json.dump(list(range(10)), f, indent=4)

with open(path, "r", encoding="utf-8") as f:
    json_result = json.load(f)
    print(json_result)

# add datas json
# so read - append - write back
with open(path, "r", encoding="utf-8") as f:
    content = json.load(f)
    content.append(4)

with open(path, "w", encoding="utf-8") as f:
    json.dump(content, f, indent=4)

with open(path, "r", encoding="utf-8") as f:
    json_result = json.load(f)
    print(json_result)

# usage of pathlib
print(Path.home())  # user directory
print(Path.cwd())  # current working directory

p = Path.home()
print(p / "dev")  # alors là cette syntaxe me la coupe un peu
print(p / "dev" / "oc-courses")
print(p.joinpath("dev", "oc-courses"))
print(p.exists())
print(p.is_dir())
print(p.is_file())  # transparents
print(p.parent.parent)
print(dir(p))

wd = Path.cwd()
print(wd)
wd = wd / "test"
wd.mkdir(exist_ok=True)
wd = wd / "a" / "b" / "c"
wd.mkdir(parents=True, exist_ok=True)
wd = wd / "readme.txt"
wd.touch() # crée fichier comme bash
wd.unlink() # = rm
wd = wd.parent
print(wd)
wd.rmdir()
wd = wd.parent.parent
# wd.rmdir() #impossible pcq a contient b

shutil.rmtree(wd) # delete dossier - attention a la cible mdr ! - permet de supprimer une arbo

wd = wd.parent / "a" / "b" / "c"
wd.mkdir(parents=True, exist_ok=True)
wd = wd / "readme.txt"
wd.touch() # crée fichier comme bash

wd.write_text("coucou")
print(wd.read_text())
wd = wd.parent.parent.parent.parent.parent
print(wd)

print(wd.iterdir())

for f in wd.iterdir():
    print(f.name)

print([f.name for f in wd.iterdir() if f.is_dir()])
print([f.name for f in wd.iterdir() if f.is_file()])

for f in wd.glob("*.py"):
    print(f.name)

# for f in wd.parent.rglob("*.py"):
#     print(f.name) # oof trop de résultats

wd = wd / "image.png"
wd.touch()
wd = wd.parent / (wd.stem + "-lowres" + wd.suffix)
wd.touch()
wd.unlink()
wd = wd.parent / "image.png"
wd.unlink()
shutil.rmtree(wd.parent / "test")


