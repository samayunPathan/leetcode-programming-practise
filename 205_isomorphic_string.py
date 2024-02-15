def isomorphic(s,t):
    if len(s)!=len(t):
        return False
    if len(set(s))!=len(set(t)):
        return False
    n=zip(s,t)
    # m=set(n)
    # print(m)
    # print(len(set(n)))
    return len(set(s))==len(set(t))==len(set(n))



# s = "egg"; t = "add"
# s = "foo"; t = "bar"
s = "paper";t = "title"
# s="bbbaaaba"
# t="aaabbbba"
print(isomorphic(s,t))