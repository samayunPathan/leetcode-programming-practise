def majority(nums):
    return list(set([i for i in nums if nums.count(i)>len(nums)//3]))
    # k=len(nums)/3
    # d={};res=[]
    # for i in nums:
    #     d[i]=nums.count(i)
    # for i in d:
    #     if d[i]>k and i not in res:
    #         res.append(i)
    # return res


    



nums = [2,3,4]
print(majority(nums))