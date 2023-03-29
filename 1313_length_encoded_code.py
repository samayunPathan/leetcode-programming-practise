def length_encoded(nums):
    res=[]
    for j in range(0,len(nums)-1,2):
        for i in range(nums[j]):
            res.append(nums[j+1])
    return res
l=[1,2,3,4]
print(length_encoded(l))
