def two_point(nums,x):
    nums=sorted(nums)
    print(nums)
    i=0;j=len(nums)-1
    while(i<=j):
        sum=nums[i]+nums[j]
        if sum==x:
            return [i,j]
        elif sum<x:
            i+=1
        elif sum>x:
            j-=1
    return False
num=[3,2,4]
print(two_point(num,6))