nums=[1,2,3,4];target=6;a=0;b=0
for i in range(len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]+nums[j]==target:
            a=i;b=j
            
print(a,b)