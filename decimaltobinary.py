def dtoB(n):
    n=int(n)
    s=''
    while n>=1:
        s+=str(n%2)
        n=n//2
    return s[::-1]
print(dtoB(6))

# ------   recursive function  -------- 
def DtoB(n):
    if n>=1:
        DtoB(n//2)
    print(n%2,end=' ')
print(DtoB(6))
