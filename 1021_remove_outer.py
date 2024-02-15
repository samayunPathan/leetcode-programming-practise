def remove_outer(s):
    c=0;st=0
    res=''
    for i,j in enumerate(s):
        if j =='(':
            c+=1
        if j==')':
            c-=1
        if c==0:
            res+=s[st+1:i]
            st=i+1
    return res
s = "(()())(())(()(()))"
print(remove_outer(s))
