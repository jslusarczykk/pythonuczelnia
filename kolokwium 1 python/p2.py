def f(x):
    if x==1 :
        return 0
    if x==2 :
        return 1
    else:
        return f(x-1) + f(x-2)

print(f(5))
print(f(9))
print(f(11))