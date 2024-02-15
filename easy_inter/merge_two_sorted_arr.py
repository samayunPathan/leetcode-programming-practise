def merge(nums1,nums2,m,n):
    for i in range(m,m+n):
        nums1[i]=(nums2[i-m])
    return nums1
    

nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
# nums1=[1,2,4,5,6,0]
# m=5
# nums2=[3]
# n=1
print(merge(nums1,nums2,m,n))