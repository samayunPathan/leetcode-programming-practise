nums=[1,3,4,5]
target=int(input())
c=None
if target not in nums:
    nums.append(target)
    nums.sort()
for i in range(len(nums)):
    if target==nums[i]:
        c=i
print(c)