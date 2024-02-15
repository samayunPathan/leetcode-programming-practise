def next_greater(nums1,nums2):
    l1=len(nums1);l2=len(nums2)
    stack=[]
    for i in range(l1):
        for j in range(l1):
            if nums1[i]==nums2[j]:
                if nums2[j+1]>nums2[j]:
                    stack.append(nums2[j+1])
                else:
                    stack.append(-1)
    return stack

nums1 = [4,1,2]
nums2 = [1,3,4,2]
print(next_greater(nums1,nums2))