def DtoB(a,b):
    c=bin(int(a,2)+int(b,2))
    # c=bin(c)
    return c.replace('0b','')
print(DtoB('11','1'))