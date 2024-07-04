arr=[[True,False],[True,True],[False,False]]

for i in range(len(arr)):
    for elem in range(2):
        if arr[i][elem]==True:
            arr[i][elem]=False
        elif arr[i][elem]==False:
            arr[i][elem]=True

#arr[0][1]=True
print(arr)

arr2 = [[True, False], [True, True], [False, False]]

for i in range(len(arr2)):
    for elem in range(2):
        arr2[i][elem] = not arr2[i][elem]

print(arr2)