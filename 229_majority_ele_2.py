from collections import Counter
def majority(nums):
    k=len(nums)//3
    d=Counter(nums)
    return [i for i,j in d.items() if j>k]
    # k=len(nums)/3
    # d={};res=[]
    # for i in nums:
    #     d[i]=nums.count(i)
    # for i in d:
    #     if d[i]>k and i not in res:
    #         res.append(i)
    # return res


    



nums = [3,2,3]
print(majority(nums))