b = "Mr. John May, born on 1998-02-16"
#b = "Hello, World!"
#print(b[-5:-2])

desc=str(input("Give me an example: "))
print(desc)

#uogólnienie
empty=" "
beg=0
end=999 #?
name=""
surname=""
initials=""
born=""
for i in range(len(desc)):
    if(desc[i]==empty):
        beg=i+1
        continue 
    for i in range(beg,len(desc)):
        if(desc[i]==empty):
            end=i-1
            name=desc[beg:end]
            print(name)


#??? 

#print("Name: ",desc[4:8])
#print("Surname: ",desc[9:8])