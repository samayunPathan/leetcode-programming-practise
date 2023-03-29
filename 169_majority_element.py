def majority(nums):
    d={}
    for i in nums:
        d[i]=nums.count(i)
    val=list(d.values())
    p=list(d.keys())
    position=val.index(max(val))
    return p[position]
n = [3,3,4]
print(majority(n))