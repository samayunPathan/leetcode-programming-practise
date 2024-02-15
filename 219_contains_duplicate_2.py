# def con_dup(nums,k):
#     l=len(nums);n=0
#     for i in range(l):
#         for j in range(i+1,l):
#             if nums[i]==nums[j] and abs(i-j)<=k:
#                 return True
#     return False
def con_dup(nums,k):
    i=0;l=len(nums)-1
    while i<l:
        if nums[i]==nums[l] and abs(i-l)<=k:
            return True
        i+=1
    return False
nums = [1,0,1,1] 
k = 1
print(con_dup(nums,k))
