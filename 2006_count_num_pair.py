def count_numpair(nums,k):
    l=len(nums);c=0
    for i in range(l):
        for j in range(i+1,l):
            if abs(nums[i]-nums[j])==k:
                c+=1
    return c
    
nums=[1,2,2,1]
print(count_numpair(nums,1))