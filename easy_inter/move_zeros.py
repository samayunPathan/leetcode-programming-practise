def move_zero(nums):
    l=len(nums)
    for i in range(l):
        if nums[i]==0:
            n=nums[i]
            nums.remove(n)
            nums.append(n)
    return nums            

nums = [0,1,0,3,12]
print(move_zero(nums))