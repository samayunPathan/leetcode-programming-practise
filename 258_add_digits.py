def add_digits(n):
    s=0
    if n<10:
        return n
    else:
        while n>=10:
            s=0
            for i in str(n):
                s+=int(i)
            n=s
    return s

n=10
print(add_digits(n))