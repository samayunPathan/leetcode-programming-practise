def reshape(mat,r,c):
    n=len(mat);m=len(mat[0]);res=[];i=0
    if n*m==r*c:
        for i in range(r):
            res.append([mat[j][k] for j in range(n) for k in range(len(mat[j]))])

            
    return res


    

mat = [[1,2],[3,4]]
r = 4
c = 1
print(reshape(mat,r,c))
