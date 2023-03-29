def trans(matrix):
    res=[];l=len(matrix)
    for i in range(len(matrix[0])):
        res.append([matrix[j][i]for j in range(l)])
    return res

matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(trans(matrix))