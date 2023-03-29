def delete_c(strs):
    res=[];ans=[];c=0
    for i in strs:
        for j in i:
            res.append(ord(j))
        ans.append(res)
        res=[]
    for i in ans:
        print(i,sorted(i),sorted(i,reverse=True))
        if sorted(i)==i or sorted(i,reverse=True)==i:
            c+=1
    print(c)
    return len(strs)-c
# strs =  ["cba","daf","ghi"]
strs=["zyx","wvu","tsr"]
print(delete_c(strs))