def search_2d_matrix(mat,target):
    if len(mat)==0: return False
    row=len(mat)
    col=len(mat[0])
    low=0;high=row*col
    
    while low<high:
        mid=(low+high)//2
        if mat[mid//col] [mid%col]==target:
            return True
        elif mat[mid//col] [mid%col] < target:
            low+=1
        else:
            high-=1
    return False
L=[[1,3,5,8],[10,11,15,16],[24,27,30,31]]
print(search_2d_matrix(L,10))

