winter_semester = {
    "math":60,
    "programming":30,
    "history":15
}

suma=0
for key,value in winter_semester.items(): #myśleć
    suma+=value

print(f"The total number of hours in the winter semester is{suma}")