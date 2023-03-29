def sum_odd_arr(nums):
    s=0;res=[]
    for i in range(1,len(nums),2):
        for j in range(i):
            res.append([j])
    print(res)
arr = [1,4,2,5,3]
print(sum_odd_arr(arr))