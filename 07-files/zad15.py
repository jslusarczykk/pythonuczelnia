f = open("zad15.txt")
for line in f:
     print(line, end="")
f.close()

print()
print()

with open("zad15.txt", "r") as f:
    for line in f:
        print(line, end="")