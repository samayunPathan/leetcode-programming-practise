def step_reduce(n):
    i=0
    while n>0:
        if n%2==0:
            n=n//2
            i+=1
        else:
            n-=1
            i+=1
    return i
print(step_reduce(14))
        