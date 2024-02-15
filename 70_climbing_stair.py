def climb_stair(n):
    s=r=1
    for i in range(1,n+1):
       
        s*=i
    for j in range(1,n):
        r*=j
       
    print(s,r)
    return (s//r)
print(climb_stair(4))