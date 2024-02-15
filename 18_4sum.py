def four_sum(nums,target):
    nums.sort()
    lth=len(nums)
    res=set();sum=0
    for i in range(lth):
        for j in range(i+1,lth):
            k=j+1
            l=lth-1
            while k<l:
                sum=nums[i]+nums[j]+nums[k]+nums[l]
                if sum<target:
                    k+=1
                elif sum>target:
                    l-=1
                else:
                    res.add((nums[i],nums[j],nums[k],nums[l]))
                    k+=1
                    l-=1
    return list(res)

nums = [1,0,-1,0,-2,2]
target = 0

print(four_sum(nums,target))