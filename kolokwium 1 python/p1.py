def f(x): #590
    if(len(x)==13 and x[:3]=="590"):
        return True
    return False

print(f("1234567890"))
print(f("5901234567890"))
print(f("59012345"))
    