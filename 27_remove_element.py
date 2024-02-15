def remove_ele(nums,val):
    while val in nums:
        nums.remove(val)

    return nums        

nums = [0,1,2,2,3,0,4,2]
val = 2
print(remove_ele(nums,val))