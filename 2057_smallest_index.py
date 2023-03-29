def smallest_in(nums):
    ans=[i for i in range(len(nums)) if i%10==nums[i]]
    return min(ans) if ans else -1
nums = [4,3,2,1]
print(smallest_in(nums))