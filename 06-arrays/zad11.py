lista=["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
longest_name=""
dlugoscstr=0
for i in range(len(lista)):
    if(len(lista[i])>dlugoscstr):
        dlugoscstr=len(lista[i])
        longest_name=lista[i]

print(longest_name)