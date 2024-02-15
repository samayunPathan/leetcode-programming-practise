def separation_arr(nums):
    ans=[]
    for i in nums:
        if len(str(i))>1:
            for j in str(i):
                ans.append(int(j))
        else:
            ans.append(i)
    return ans

nums=[7,1,3,9]
print(separation_arr(nums))