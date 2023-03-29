def happy(n):
    s=0
    if n==1:
        return True
    else:
        while n>1:
            s=0
            for i in str(n):
                s+=(int(i)*int(i))
            n=s
        return True if s==1 else False

print(happy(1))