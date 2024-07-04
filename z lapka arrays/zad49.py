arr=[[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for i in range(1,len(arr)+1):
    arr[i-1][0]=i
    arr[i-1][1]=i*2
    arr[i-1][2]=i*3
    arr[i-1][3]=i*4
    arr[i-1][4]=i*5

print(arr)
