# from collections import counter
def uncommon(s,t):
    s=list(set(s.split(' ')));t=list(set(t.split(' ')));d={}
    ns=s+t
    for i in ns:
        d[i]=ns.count(i)
    return[i for i,j in d.items() if j==1]
    



# s1 = "this apple is sweet"; s2 = "this apple is sour"
s1 = "apple apple";s2 = "banana"
print(uncommon(s1,s2))