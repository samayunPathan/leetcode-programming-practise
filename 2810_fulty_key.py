def fulty_key(s):
    ans=''
    for i in s:
        if i=='i':
            n=ans
            ans=''
            ans+=n[::-1]
        else:
            ans+=i
    return ans
s = "string"
print(fulty_key(s))