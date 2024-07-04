plik = input("Enter file name: ")

plik1 = open(plik)

x=plik1.readline()
counter=0
while x!="":
    counter+=1
    #print(counter, x)
    x=plik1.readline()

print(counter)
plik1.close()
