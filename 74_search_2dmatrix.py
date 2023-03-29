def search_2d_matrix(nums,target):
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if target==nums[i][j]:
                return True
    return False
l=[[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(search_2d_matrix(l,3))
