def sum_odd_arr(nums):
    s=0
    for i in range(len(nums)):
        for j in range(1,len(nums)):
            print(nums[0:j:2])
           

    return s

l=[1,2,3,4,5]
print(sum_odd_arr(l))