import math
grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]
AOOG = len(grades) #amount of original grades
#grades higher than 2.0
GHT2=list(filter(lambda x:x>2.0,grades))
AOG=len(GHT2)
sum=0
for i in range(len(GHT2)):
    sum+=GHT2[i]
print(math.floor(sum/AOG*100)/100)