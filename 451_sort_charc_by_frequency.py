from collections import Counter
def sort_char(s):
    ans=''
    c=Counter(s)
    print(c)
    m=sorted(c.items(),key=lambda x:x[1],reverse=True)
    print(m)
    for i in m:
        print(i[1])
        ans+=i[0]*i[1]
    return ans
s ="Aabb"
s ="tree"
print(sort_char(s))
