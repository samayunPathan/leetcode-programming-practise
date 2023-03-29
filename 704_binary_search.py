l=[-1,0,3,5,7,9,10]
l1=[5]
def binary_search(nums,target):
    lo=0;hi=len(nums)-1
    while lo<=hi:
        mid=lo+(hi-lo)//2
        if target==nums[mid]:
            return mid
        elif target<nums[mid]:
            hi=mid-1
        else:
            lo=mid+1
    return -1
print(binary_search(l1,5))

