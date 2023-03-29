def circle_s(s):
    s=s.split(' ');c=0;i=0
    l=len(s)
    if l<2:
        if s[0][0]==s[0][-1]:
            return True
    else:
        i=0
        while i<l-1:
            if s[i][-1]==s[i+1][0]:
                c+=1
            i+=1
    return c==l-1 and s[0][0]==s[-1][-1]

s= "Leetcode"
print(circle_s(s))