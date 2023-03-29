def lucky(matrix):
    res=[];c=0
    for i in matrix:
        res+=[min(i)]
    m=max(res)
    print(m)
    for i in range(len(matrix)):
        if m in matrix[i]:
            c=i
    print(matrix[c])
    if m==min(matrix[c]):
        return m
    


matrix =[[3,6],[7,1],[5,2],[4,8]]
print(lucky(matrix))