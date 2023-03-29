def attendence(s):
    a=0;l=0;c=0
    for i in s:
        if i=='A':
            a+=1
    for i in range(len(s)-1):
        if s[i]=='L':
            if s[i]==s[i+1]:
                c+=1
            else:
                c=0
        if c>2:
            break               
    return a<2 and c<2

s="PPALLL"

print(attendence(s))