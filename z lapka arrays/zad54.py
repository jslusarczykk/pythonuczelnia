#transpozycja macierzy = rows into columns and columns into rows
def transpose_matrix(arr):
    if str(arr):
        return arr
    arr2=[[0 for i in range(len(arr))]for j in range(len(arr[0]))]
    for i in range(len(arr2[0])):                                               #for i in range(len(arr2[0])):
        for j in range(len(arr2)):                                                      #arr2[0][i]=arr[i][0]
            arr2[j][i]=arr[i][j]
        
    return arr2

if __name__ == 'main':
    arr=[[1,2,3,4,5],[3,5,6,3,2],[0,0,0,1,0]]
    print(transpose_matrix(arr))


       