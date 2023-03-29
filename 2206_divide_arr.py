def divide_arr(nums):
    c=0;l=len(nums)
    for i in range(l-1):
        for j in range(i,l-1):
            if nums[i]+nums[j]==nums[i]*2:
                c+=1
    return c==l//2
nums=[3,2,3,2,2,2]
print(divide_arr(nums))
