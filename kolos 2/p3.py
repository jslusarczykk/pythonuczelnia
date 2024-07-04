def f(c): #suma kart
    sum=0
    for i in range(len(c)):
        if c[i]=="A" or c[i]=="K" or c[i]=="Q" or c[i]=="J" or c[i]=="T":
            sum+=10
        else:
            sum+=int(c[i])
    return sum

print(f("2K9"))
print(f("234AJ7"))