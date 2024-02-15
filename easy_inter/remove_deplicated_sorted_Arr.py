def remove_dep(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[i] != nums[j]:
            i += 1
            nums[i] = nums[j]
            # nums.remove(nums[j])
    return set(nums),i+1


nums=[1,1,1,1]
nums = [0,0,1,1,1,2,2,3,3,4]
# nums = [1,1,2]
print(remove_dep(nums))