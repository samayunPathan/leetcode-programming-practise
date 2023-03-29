def odd_avg(nums):
    res=[]
    for i in nums:
        if i%2==0 and i%3==0:
            res.append(i)
    if len(res)==0:
        return 0
    elif len(res)==1:
        return res[0]
    else:
        return sum(res)//len(res)

nums =  [4,4,9,10]
print(odd_avg(nums))