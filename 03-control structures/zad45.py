
N=int(input("Enter N: "))
count=0
x=3
print("2")

while(count<N):
    czypierwsza=1
    for i in range(2,x):
        if(x%i==0):
            czypierwsza=0
            
    if(czypierwsza==1):
        print(x, end=" ")
        count+=1
    x+=1
        
       
#        if(N%j==0):
 #           niepierwsza=True
  #          break
   # if not niepierwsza:
    #    print(i, end=" ")
       
            