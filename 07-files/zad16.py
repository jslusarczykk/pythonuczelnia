plik = input("Enter file name: ")

plik1 = open(plik)
lines=0
for line in plik1:
    lines+=1
print(lines)
#plik1.close()

