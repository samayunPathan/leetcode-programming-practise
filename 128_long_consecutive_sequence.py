def long_cons(nums):
    if len(nums)<1:
        return 0
    res=[]
    nums=list(set(nums))
    nums.sort()
    print(nums)
    res.append(nums[0])
    for i in range(len(nums)-1):
        if abs(nums[i+1]-nums[i])==1:
            print(nums[i+1])
            res.append(nums[i+1])
    return len(res)
nums = [0,3,7,2,5,8,4,6,0,1]
nums = [100,4,200,1,3,2]
nums=[1]
nums=[]
nums =[9,1,4,7,3,-1,0,5,8,-1,6]
print(long_cons(nums))