def product(nums):
    mul=1
    if nums.count(0)>=1:
        return 0
    else:
        for i in nums:
            mul*=i
    print(mul)
    return -1 if mul<0 else 1

n=[-1,1,-1,1,-1]
print(product(n))