def keep_mul(nums,original):
    i=0
    while i<=len(nums):
        if original in nums:
            original=original*2
        i+=1
    return original

nums = [5,3,6,1,12]; original = 3
print(keep_mul(nums,original))