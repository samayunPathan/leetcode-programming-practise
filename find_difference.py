s='a';t='aa'
s=set(s);t=set(t)

if len(s)>len(t):
    for i in s:
        if i not in t:
            print(i)
else:
    for i in t:
        if i not in s:
            print(i)


# cheak=set(s)
#         for x in t:
#             if x not in cheak:
#                 return x
#             if s.count(x)!=t.count(x):
#                 return x
        
    


