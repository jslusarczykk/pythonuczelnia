import json
#data: name, surname, student ID, gender, age, year of study, email

#limited.json first, last name id

with open("students.json") as file:
    data = json.load(file)