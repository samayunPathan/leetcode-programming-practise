n=input()
a='';i=0
for i in range(i,len(n)):
    if n[i] not in a:
        a+=n[i]
    else:
        i=i
        
print(a)