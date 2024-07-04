#the same number of rows and columns
def f(arr): #arr=[[3,7,2],[4,2,5],[5,2,1]]
    sum_row=0
    sum_column=0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            sum_row+=arr[j][i]
            sum_column+=arr[i][j]
        if sum_row!=sum_column:
            return False
    return True

print(f([[3,7,2],[4,2,5],[5,2,1]]))
print(f([[3,7,2],[4,2,5],[9,2,1]]))
