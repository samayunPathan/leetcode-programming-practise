def target_indices(nums,target):
    nums.sort()
    return [i for i in range(len(nums)) if nums[i]==target]
n=[1,2,5,2,3]
target = 2
print(target_indices(n,target))
