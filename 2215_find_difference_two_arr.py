def find_difference(nums1,nums2):
    ls=list(set(nums1)-set(nums2))
    ls2=list(set(nums2)-set(nums1))
    return [ls]+[ls2]
nums1 = [1,2,3]; nums2 = [2,4,6]
print(find_difference(nums1,nums2))