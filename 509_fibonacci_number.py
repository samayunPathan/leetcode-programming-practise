def fibonacci(n):
    i=0;j=1
    if n==1:
        return 0
    elif n==1:
        return 1
    else:
        ans=0
        for i in range(n):
            print(i,j,ans)
            ans=i+j
            i=j
            j=ans
            ans=0
            # print(i,j,ans)
            # print(ans)
    return ans
print(fibonacci(4))
