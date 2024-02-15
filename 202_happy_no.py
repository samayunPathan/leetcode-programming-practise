def happy_no(n):
    m=str(n)
    if len(m)<2:
        return False
    else:
        sum=0;i=0
        while sum>1:
            for i in range(len(m)):
                sum+=int(m[i])**2
        if sum==1:
            return True
        return False


print(happy_no(12))
