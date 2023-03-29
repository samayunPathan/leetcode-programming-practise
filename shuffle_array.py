l=[1,2,3,4,5,6]
def shuffle_func(nums,n):
    nums_f=[];i=0
    while i<n:
        nums_f.append(nums[i]),nums_f.append(nums[n+i])
        i+=1
    return nums_f
print(shuffle_func(l,3))