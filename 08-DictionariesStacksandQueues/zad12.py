import json

file = open("student.json",'w')

student_data={
    "Height":184,
    "Weight":"70kg",
    "animals":{"cat":"Ragdoll","dog":"White swiss shepherd"},
    "Grades":[2,6,3,4,5,6],
    "Wintrader":True
}

json.dump(student_data,file,indent=2)

file.close()