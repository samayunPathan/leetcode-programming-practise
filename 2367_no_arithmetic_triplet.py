def arith_trip(nums,diff):
    res=0
    for i in range(len(nums)):
        j=i+1
        k=len(nums)-1
        while j<k:
            val=nums[j]-nums[i]
            ans=nums[k]-nums[j]
            if val==diff and ans==diff:
                res+=1
                k-=1
                j+=1
            elif val<diff:
                j+=1
            else:
                k-=1           
    return res

# nums = [0,1,4,6,7,10]
# diff = 3
nums = [4,5,6,7,8,9]
diff = 2
print(arith_trip(nums,diff))