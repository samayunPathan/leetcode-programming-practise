def missing(nums):
    res=[i for i in range(len(nums)+1)]
    r= list(set(res)-set(nums))
    return r[0]

nums = [9,6,4,2,3,5,7,0,1]
print(missing(nums))