def trancate(s,n):
    s=s.split(' ');res=[]
    for i in range(n):
        res.append(s[i])
    return ' '.join(res)
s = "Hello how are you Contestant"
k = 4
print(trancate(s,k))