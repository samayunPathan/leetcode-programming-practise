def lucky(arr):
    res=[]
    for i in arr:
        if i==arr.count(i):
            res.append(i)
    print(res)
    return max(res) if len(res)>=1 else -1


n=[19,12,11,14,18,8,6,6,13,9,8,3,10,10,1,10,5,12,13,13,9]
print(lucky(n))