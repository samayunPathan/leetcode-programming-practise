def depth_paren(s):
    res=0;cur=0
    for i in s:
        if i=='(':
            cur+=1
            res=max(res,cur)
        if i==')':
            cur-=1
    return res

s = "(1+(2*3)+((8)/4))+1"
print(depth_paren(s))