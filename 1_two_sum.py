def two_sum(nums,target):
    res=[];a=0;b=0
    for i in range(len(nums)-1):
        if nums[i]+nums[i+1]==target:
            a=i;b=i+1
        
    return a,b


nums=[2,11,7,15]
print(two_sum(nums,9))

