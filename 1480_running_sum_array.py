def running_sum_array(nums):
    s=[];c=0
    for i in range(len(nums)):
        for j in range(i+1):
            c+=nums[j]
        s.append(c)
        c=0
    return s
l=[1,2,3,4]
print(running_sum_array(l))
