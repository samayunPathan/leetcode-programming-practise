def sum_op(nums):
    c=0
    for i in nums:
        if '+' in i:
            c+=1
        elif '-' in i:
            c-=1
    return c