arr=[[-38, 19], [5,40],[-7,11],[29,16]]
#smallest and largest number and their position

largest=0
largest_position=[0,0]
smallest=999
smallest_position=[0,0]

for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] > largest :
            largest_position[0]=i
            largest_position[1]=j
            largest=arr[i][j]
        if arr[i][j] < smallest :
            smallest_position[0]=i
            smallest_position[1]=j
            smallest=arr[i][j]
            
print(largest," ",largest_position," ",smallest," ",smallest_position)
