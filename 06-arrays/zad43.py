#b.	A function that returns an ordered array of words, from longest to shortest
#c.	A function that returns an alphabetically ordered array of words
def a(x): #a.	A function that returns the number of words in the text
    count=1
    for i in range(len(x)-1):
        if(x[i]==" "):
            count+=1
    return count
def b(x):
    return 0
if __name__ == 'main':    
    x="An apple a day keeps the doctor away"
    print(a(x))