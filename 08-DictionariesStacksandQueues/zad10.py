import json

with open("sample1.json") as file:
    data = json.load(file)

for key,value in data.items():
    print(f"{key} : {value}")
