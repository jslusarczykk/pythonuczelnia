import math
a=float(input("Enter a: "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))

p=(a+b+c)/2
value=p*(p-a)*(p-b)*(p-c)
tarea=math.sqrt(value)
tcircumference=a+b+c

print(f"Triangle circumference is: {tcircumference}")
print(f"Triangle area is: {tarea}")