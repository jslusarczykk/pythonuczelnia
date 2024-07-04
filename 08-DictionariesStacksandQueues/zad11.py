import json
file=open("favourite.json",'w')

movie = {
    "title":"Harry potter",
    "year": 2035,
    "actor":{"leading":"Nie wiem","supporting":"Nie mam pojecia"},
    "oscar":True,
    "cat":{"black":"hermiona","white":"harry"}
}

json.dump(movie, file, indent=1) #INDENT OZNACZA DWIE SPACJE W KODZIE

print(f"The data has been written to {file}.")

file.close()