def reverse_arr(nums):
    for i in range(len(nums)//2):
        l=nums[i]
        # nums[i]=nums[-i-1]
        nums[i]=nums[~i]
        nums[-i-1]=l
    return nums
n=[1,2,3,4,5,6]
print(reverse_arr(n))

# def reverse_arr_recursive(nums):
#     if 