# s=input('enter input strings : ')
s='pwwke'
n='';j=0;k=0

for i in range(len(s)):
    if s[i] not in n:
        n+=s[i]
    elif s[i] in n:
        n=n.replace(n,"")
        
            
 
print(n)

# m='pwwkew'
# m=m.replace(m,'')
# print(m)