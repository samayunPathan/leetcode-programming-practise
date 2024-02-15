def max_depth(s):
    res=cur=0
    for i in s:
        if i=='(':
            cur+=1
            res=max(res,cur)
        elif i==')':
            cur-=1
    return res
    
    

s = "(1+(2*3)+((8)/4))+1"
print(max_depth(s))