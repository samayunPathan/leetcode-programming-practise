def intersection_arr(nums1,nums2):
    nums1.sort();nums2.sort()
    res=[];i=j=0
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<nums2[j]:
            i+=1
        elif nums1[i]>nums2[j]:
            j+=1
        else:
            res.append(nums1[i])
            i+=1
            j+=1
    return res
nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersection_arr(nums1,nums2))