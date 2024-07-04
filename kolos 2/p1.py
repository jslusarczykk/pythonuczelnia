def f(e): #2+3 = 5 #2+3-4+5-0  = 6
    sum=0
    sum+=int(e[0])
    for i in range(1,len(e)-1):
        if e[i]== "+" :
            sum+=int(e[i+1])
        elif e[i]=="-":
            sum-=int(e[i+1])
    return sum

print(f("2+3-4+5-0"))
print(f("3+8+1"))
print(f("2+3"))