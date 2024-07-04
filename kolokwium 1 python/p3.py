def ilosccyfr(x):
    counter=0
    while(x>0):
        x=x//10
        counter+=1
    return counter

def f(x):
    sum=0
    seen_numbers = set()
    for i in range(ilosccyfr(x)):
        if i not in seen_numbers:
            seen_numbers.add(i)
        else:
            sum+=seen_numbers(i)+i
            seen_numbers.remove(i)
    return sum
print(f(230335))