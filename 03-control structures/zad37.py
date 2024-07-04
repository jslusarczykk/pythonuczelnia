
max_number=5

for i in range(0,6,1):
    for j in range(i):
        print("*",end=" ")
    print()

for i in range(max_number - 1, 0, -1):
    for j in range(i):
         print("*",end=" ")
    print()