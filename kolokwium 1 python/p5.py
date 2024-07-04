def f(a,b):
    seen_chars = []
    for i in range(a,b-1,-1):
        seen_chars.append(i)
    return seen_chars
print(f(5,2))
print(f(2,1))
print(f(43,41))