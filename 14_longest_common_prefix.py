def logestest_word(strs):
    res=sorted(strs)
    ans=''
    fast=res[0];last=res[-1]
    for i in range(min(len(fast),len(last))):
        if fast[i]!=last[i]:
            return ans
        ans+=fast[i]
    
strs=['rlow','flaws','flat']
print(logestest_word(strs))