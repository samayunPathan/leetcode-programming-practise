def fliping_image(nums):
    for i in range(len(nums)):
        for j in range(len(nums[i])):
            if nums[i][j]==0:
                nums[i][j]=1
            else:
                nums[i][j]=0
    return nums


n=[[0,1,0],[1,0,1],[0,0,0]]
print(fliping_image(n))
# if n[0][0]==1:
#     print('yes')