#[[1,2,3,4],[5,6,7,8]]-->[[5,6,7,8],[1,2,3,4]]
def f(arr):
    x=arr[0]
    #print(arr2)
    arr[0]=arr[-1]
    arr[len(arr)-1]=x #to nie dziala sus???? XDDDDD????? X?D?D ?XD? ?czemu niby to nie dzialalo wczesniej
    return arr

print(f([[1,2,3,4],[5,6,7,8]]))
print(f([[1,1],[2,2],[3,3],[4,4]]))