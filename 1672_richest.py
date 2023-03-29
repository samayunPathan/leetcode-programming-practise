def richest(accounts):
    s=[]
    for i in range(len(accounts)):
        s.append(sum(accounts[i]))
    return max(s)




l=[[1,2],[3,4],[5,6]]
print(richest(l))
