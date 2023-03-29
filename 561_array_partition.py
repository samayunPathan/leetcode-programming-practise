def arr_partition(nums):
    nums.sort();s=0
    for i in range(0,len(nums),2):
        # print(i)
        s+=nums[i]
        # print(s)
    return s
n=[6,2,6,5,1,2]
print(arr_partition(n))

# for i in range(0,4,2):
#     print(i)