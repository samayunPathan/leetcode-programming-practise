def reve_vowel(s):
    d={}
    ls=['a', 'e', 'i', 'o','u']
    n=''
    for i,j in enumerate(s):
        d[i]=j
    for i in d.values():
        if i.lower() in ls:
            n+=i

    n=n[::-1]
    print(n)
    j=0
    lst=list(d.values())
    for i in range(len(lst)):
        if lst[i].lower() in ls:
            lst[i]=n[j]
            j+=1
     
    return ''.join(list(lst))
s = "leetcode"
s ="aA"
print(reve_vowel(s))