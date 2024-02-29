def k_most(l,k):
    d={}
    for i in range(len(l)):
        d[l[i]]=l.count(l[i])
    ls=sorted(d,key=lambda x:d[x],reverse=True)
    return ls[:k]
n=[1,1,1,2,2,3,4,4,4,4]
# n=[1,2]
print(k_most(n,2))