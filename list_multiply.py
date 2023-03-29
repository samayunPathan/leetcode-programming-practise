l=[-1,1,0,-3,3]
s=1;j=0;d=0
c=[]
while j<len(l):
    for i in range(len(l)):
        s*=l[i]
    if l[j]!=0:
        d=s//l[j]
        c.append(d)
    else:
        c.append()
    s=1
    j+=1
print(c)
