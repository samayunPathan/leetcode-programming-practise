def rotate_arr(nums,k):
    i=0
    while i<k:
        nums.insert(0,nums[-1])
        nums.pop()
        i+=1
    return nums
nums = [-1,-100,3,99]; k = 2
print(rotate_arr(nums,k))