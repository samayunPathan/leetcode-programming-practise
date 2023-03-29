def k_most(l,k):
    ls=[]
    for i in l:
        if l.count(i)>=k:
            print(i)
            ls.append(i)
    return list(set(sorted(ls)))
n=[1,1,1,2,2,3]
print(k_most(n,2))