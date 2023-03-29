def unique_occurance(nums):
    d={}
    for i in nums:
        d[i]=nums.count(i)
    val=list(d.values())
    return  len(val)-len(set(val))==0

arr = [1,3]
arr2=[-3,0,1,-3,1,1,1,-3,10,0]
print(unique_occurance(arr))