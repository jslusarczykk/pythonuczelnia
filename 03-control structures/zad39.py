a=int(input("Enter a: "))
b=int(input("Enter b: "))

#a=wysokosc b=szerokosc
#a=4 b=15
# ***************
# *             *
# *             *
# ***************
for j in range(b):
    print("*", end="")
print()
for i in range(2,a):
    print("*", end=" ")
    for j in range(2,b-1):
        print("",end=" ")
    print("*",end=" ")
    print()
    
for j in range(b):
    print("*", end="")
print()