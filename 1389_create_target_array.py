# nums=[1,3,5];index=[0,2,4]
# print(nums[2:2])
# res=[]
# # for i,j in zip(nums,index):
# #     res[i:i]=j
# # print(res)

# nums=set([2,3,4])
# nums2=set([3,3,4,5])
# nums3=set([5,6,7])
# nums4=nums.union(nums2).union(nums3)
# print(nums4)


def target_arr(nums,index):
    ans=[]
    for i in range(len(nums)):
        ans.insert(index[i],nums[i])
    return ans
nums = [0,1,2,3,4]; index = [0,1,2,2,1]
print(target_arr(nums,index))
