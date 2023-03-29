def height_checker(nums):
    nums2=sorted(nums);c=0
    for i in range(len(nums)):
        if nums2[i]!=nums[i]:
            c+=1
    return c
n=[1,1,4,2,1,3]
print(height_checker(n))