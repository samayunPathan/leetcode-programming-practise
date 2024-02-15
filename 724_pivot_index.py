# def pivot_index(nums):
#     for i in range(len(nums)):
#         if sum(nums[:i])==sum(nums[i+1:]):
#             return i
        
def pivot_index(nums):
    prefix=0
    suffix=sum(nums)
    for i in range(len(nums)):
        prefix+=nums[i]
        if prefix==suffix:
            return i
        suffix-=nums[i]
        
nums=[1,7,3,6,5,6]
print(pivot_index(nums))