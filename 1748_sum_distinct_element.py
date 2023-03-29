def sum_dis(nums):
    s=[i for i in nums if nums.count(i)==1]
    return sum(s)
print(sum_dis([1,2,3,2]))


# s = 0
#         a = [s+i for i in nums if nums.count(i) == 1]
#         return sum(a)