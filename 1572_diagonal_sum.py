l=[[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
l1=[[1,2,3],[1,2,3],[1,2,3]]
def diagonal_sum(mat):
    sum=0
    if len(mat)==len(mat[0]):
        for i in range(len(mat)):
            sum+=mat[i][i]+mat[i][~i]
        if len(mat)%2:
            sum-=mat[len(mat)//2][len(mat)//2]
        
    return sum
print(diagonal_sum(l1))

