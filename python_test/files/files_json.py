import json

path = "c:/Users/alexandre.lourencinh/dev/oc-courses/python/python_test/files/my_json.json"

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
    json.dump(content, f, indent = 4)

with open(path, "r", encoding = "utf-8") as f:
    json_result = json.load(f)
    print(json_result)
