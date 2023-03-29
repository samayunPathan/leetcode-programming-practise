def sort_array_2(nums):
    res=[None]*len(nums);e=0;o=1
    for i in nums:
        if i%2==0:
            res[e]=i
            e+=2
        else:
            res[o]=i
            o+=2
    return res
num=[1,2,3,4]
print(sort_array_2(num))