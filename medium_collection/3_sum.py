def three_sum(nums):
    nums.sort()
    res=set();l=len(nums)
    for i in range(l):
        j=i+1
        k=l-1
        while j<k:
            val=nums[i]+nums[j]+nums[k]
            if val ==0:
                res.add((nums[i],nums[j],nums[k]))
                j+=1
                k-=1
            
            if val<0:
                j+=1
            elif val>0:
                k-=1
            
    return list(res)
nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))
