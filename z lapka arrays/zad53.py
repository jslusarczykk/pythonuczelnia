def identity_matrix(n) :
    arr=[[0 for i in range(n)]for j in range(n)]
    for i in range(n):
        for j in range(n):
            if i == j :
                arr[i][j]=1
    
    return arr

print(identity_matrix(3))
print(identity_matrix(5))
print(identity_matrix(8))