def f(d,v):
    sum=0
    szukana=True
    if v != True:
        szukana=False
    for key, value in d.items():
        if value!=szukana:
            sum+=1
    return sum

print(f({"a":True,"b":False,"c":True,"d":True,"e":True},True))
print(f({"a":True,"b":False,"c":True,"d":True,"e":True},False))
