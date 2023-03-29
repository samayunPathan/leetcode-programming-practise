l1=[1,2,3,4]
l2=[3,4,5,6]

def binary_search(nums1,nums2):
    nums1.sort();nums2.sort()
    i=0;j=0;l=[]
    while i<len(nums1) and j<len(nums2):
        if nums1[i]<nums2[j]:
            i+=1
        elif nums1[i]>nums2[j]:
            j+=1
        elif nums1[i]==nums2[j]:
            l.append(nums1[i])
            i+=1;j+=1
    return l
print(binary_search(l1,l2))

