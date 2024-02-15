# def three_sum(nums):
#     ls=set();ls2=[];nums.sort();length=len(nums)
#     for i in range(length):
#         for j in range(i+1,length):
#             for k in range(j+1,length):
#                 if nums[i]+nums[j]+nums[k]==0 :
#                     ls.add(tuple([nums[i],nums[j],nums[k]]))
#     return list(ls)
# l=[-1,0,1,2,-1,-4]
# print(three_sum(l))


def three_sum(nums):
    # l=len(nums)
    # nums.sort()
    # res=set();sum=0
    # for i in range(l):
    #     j=i+1
    #     k=l-1
    #     while j<k:
    #         sum=nums[i]+nums[j]+nums[k]
    #         if sum>0:
    #             k-=1
    #         elif sum<0 :
    #             j+=1
    #         else:
    #             res.add((nums[i],nums[j],nums[k]))
    #             j+=1
    #             k-=1

    # return list(res)
    res=set();sum=0
    l=len(nums)
    for i in range(l):
        j=i+1
        k=l-1
        while j<k:
            sum=nums[i]+nums[j]+nums[k]
            if sum<0:
                j+=1
            elif sum>0:
                k-=1
            else:
                res.add((nums[i],nums[j],nums[k]))
                j+=1
                k-=1
    return list(res)

nums = [-1,0,1,2,-1,-4]
print(three_sum(nums))


