def con_duplicate(nums):
    return len(set(nums))!=len((nums))

nums = [1,2,3,1]
print(con_duplicate(nums))