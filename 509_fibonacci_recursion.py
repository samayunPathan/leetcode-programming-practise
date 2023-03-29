def fibonocci_recursion(n):
    if n==0:
        return 0
    fibonocci_recursion(n)



# def fibonacci(n):
#     m=0;n=1;s=[]
#     for i in range(n):
#         s.append(m+n)
#         m=n
#         n=m+n
#     return s
# print(fibonacci(5))
s=[0,1];m=0;n=1;l=0
for i in range(5):
        l+=m+n
        s.append(l)
        m=n
        n=l
        l=0

# s.insert(0,0)
# s.insert(1,1)
print(s)