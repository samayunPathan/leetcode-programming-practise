def plus_one(digits):
    n='';l=[]
    for i in digits:
        n+=str(i)
    m=str(int(n)+1)
    for i in m:
        l.append(int(i))
    return l

digits=[9]
print(plus_one(digits))