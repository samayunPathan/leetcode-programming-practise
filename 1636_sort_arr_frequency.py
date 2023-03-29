
def sort_frequency(nums):
    d={}
    for i in range(len(nums)):
        d[nums[i]]=nums.count(nums[i])
    l=list(d.items())
    l.sort(key=lambda x:x[0],reverse=True)
    l.sort(key=lambda x:x[1])
    res=[]
    for i in l:
        a,b=i
        res.extend([a]*b)
    return res
    # r = Counter(nums)
    # return sorted(nums, key=lambda x: (r[x], -x))
    




n=[1,1,2,2,2,3]
m=[2,3,1,3,2]
print(sort_frequency(n))