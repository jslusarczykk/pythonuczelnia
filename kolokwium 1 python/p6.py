def ilosccyfr(x):
    counter=0
    while(x>0):
        x=x//10
        counter+=1
    return counter

def f(x,y):
    znaki1=[]
    znaki2=[]
    while(x or y > 0):
        for i in range(ilosccyfr(x)):
            znaki1.append(x%10)
            x=x//10
            for j in range(ilosccyfr(y)):
                if(znaki1[i]==y%10):
                    return True
                y=y//10
    return False

print(f(12,715))
print(f(1234,987654))
print(f(1234,98765))
