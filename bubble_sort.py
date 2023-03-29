from tkinter import N


nums=[2,5,3,7,8,9]
nums2=[1,2,3,4]
def bubble(nums):
    l=len(nums)
    flag=0
    for i in range(l-1):
        for j in range(l-1-i):
            if nums[j]>nums[j+1]:
                n=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=n
                flag+=1 
    if flag==0:
        return nums
    return nums
print(bubble(nums2))
            