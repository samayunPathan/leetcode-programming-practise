def group_ana(strs):
    res={}
    for i in strs:
        k=''.join(sorted(i))
        if k not in res:
            res[k]=[]
        res[k].append(i)
    return list(res.values())
strs = ["eat","tea","tan","ate","nat","bat"]
print(group_ana(strs))