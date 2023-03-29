def consecutive(nums):
    res=[];c=0
    res.append(0)
    for i in range(len(nums)):
        if nums[i]==1:
            c+=1
        else:
            res.append(c)
            c=0
    return max(res)



nums = [1,0,1,1,0,1]
print(consecutive(nums))