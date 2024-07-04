import re

def f(t):
    import re
    sum=0
    tab=re.findall("\d+" "",t)
    for i in range(len(tab)):
        sum+=int(tab[i])
    return sum

print(f("11 and 4 is 15"))
print(f("water12, and 3play is not 8"))