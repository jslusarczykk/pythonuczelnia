def f(x):
    sum=0
    for i in range(len(x)):
        if x[i] == "-" :
            sum-=1
        else:
            sum+=1
    return sum

print(f(""))
print(f("+-+"))
print(f("+-+++-+"))