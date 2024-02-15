def sum_multi(n):
    res=0
    nums=list(range(1,n+1))
    for i in nums:
        if i%3==0 or i%5==0 or i%7==0:
            res+=i
    return res


print(sum_multi(7))