employees = ["SMITH Lucy","JONES Janet","LEE Jerry",
             "JACKSON Peter","JOHNSON Rick",
             "LEWIS Terry","CLARKE Robin"]
emp_J = list(filter(lambda e:e[0]=="J", employees))
for i in range(len(emp_J)):
    print(emp_J[i])
#JONES Janet
#JACKSON Peter
#JOHNSON Rick


#jakis losowy program
arr =[2,5,4,7]
lista=list(filter(lambda x:x>4,arr))
print(lista)