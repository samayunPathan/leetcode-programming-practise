def rm_dup(nums):
    nums[:] = sorted(list(set(nums)))
n=[1,1,2,3,3,4,5,5]
print(rm_dup(n))
