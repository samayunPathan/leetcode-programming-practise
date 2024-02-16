def num_complement(n):
    b='';ans='';res=0
    while n>=1:
        b+=str(n%2)
        n=n//2
    b=reversed(b)
    for i in b:
        if i=='1':
            ans+=str(0)
        else:
            ans+=str(1)
    print(ans)
    for i in range(len(ans)):
        res+=int(ans[~i])*(2**i)
    return res
        



print(num_complement(2))