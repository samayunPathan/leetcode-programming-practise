def three_sum(nums):
    ls=set();ls2=[];nums.sort();length=len(nums)
    for i in range(length):
        for j in range(i+1,length):
            for k in range(j+1,length):
                if nums[i]+nums[j]+nums[k]==0 :
                    ls.add(tuple([nums[i],nums[j],nums[k]]))
    return list(ls)
l=[-1,0,1,2,-1,-4]
print(three_sum(l))


# def threeSum(nums):
#         output = []
		
#         for idx1, val1 in enumerate(nums[:-2]):
#             for idx2, val2 in enumerate(nums[idx1+1:-1]):
#                 for idx3, val3 in enumerate(nums[idx2+1:]):
#                     sum = val1+val2+val3
#                     if sum == 0:
#                         output.append(tuple(sorted([val1, val2, val3])))
#         return list(set(output))
# print(threeSum(l))