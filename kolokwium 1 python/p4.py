def f(x):
    lista=[]
    ciag=""
    while(x>0):
        if(x<10 and x>0):
            x=str(x)
            ciag+=x
        lista.append(x%10)
        x=x//10
    for i in range(x-1):
        print()
    return ciag

print(f(23456))
 