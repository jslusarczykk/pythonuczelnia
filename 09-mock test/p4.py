def avg_grade(marks):
    ilosc=len(marks)
    suma=0
    for i in range(len(marks)):
        suma+=int(marks[i])
    return suma/ilosc

def f(subjects): #highest grades
    highest_grade=0
    highest_grade_name=""
    for key,value in subjects.items():
        if avg_grade(subjects[key])>highest_grade: #why not working?
            highest_grade=avg_grade(subjects[key])
            highest_grade_name=key
    return highest_grade_name
    

print(f({"math":[3,4,4],"geo":[5,4,4,4],"comp":[5,4]})) 