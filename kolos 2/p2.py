def f(d): #remaining people in room
    count=0
    for i in range(len(d)):
        if(d[i]=="+"):
            count+=1
        elif d[i]=="-":
            count-=1
    return count

print(f("+-+++-+---"))
print(f("+-+++++-"))