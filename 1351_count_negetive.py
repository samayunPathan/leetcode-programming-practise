def count_nage(nums):
    c=0
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if nums[i][j]<0:
                c+=1
    return c
l=[[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
print(count_nage(l))