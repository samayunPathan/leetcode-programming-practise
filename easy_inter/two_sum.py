def two_sum(nums,target):
    i=0;j=len(nums)-1;res=[]
    nums1=sorted(nums)
    while i<j:
        sum=nums1[i]+nums1[j]
        if sum==target:
            break
        elif sum>target:
            j-=1
        elif sum<target:
            i+=1
    for k in range(len(nums)):
            if nums1[i]==nums[k]:
                res.append(k)
            elif nums1[j]==nums[k]:
                res.append(k)
    return res

        

nums=[3,2,4]
target=6
print(two_sum(nums,target))