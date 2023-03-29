def smaller_num(nums):
    # n=len(nums)
    # a=[]
    # for i in range(n):
    #     c=0
    #     for j in range(n):
    #         if i!=j and nums[j]<nums[i]:
    #             c+=1
    #     a.append(c)
    # return a
    n=sorted(nums)
    return [n.index(i) for i in nums]
   

nums1=[8,1,2,2,3]
print(smaller_num(nums1))