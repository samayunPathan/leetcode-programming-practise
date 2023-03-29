def remove_paren(s):
    ans=[None]*len(s);d={')':'('}
    for i in range(len(s)-1):
        if ans[i]!=ans[i+1]:
            ans.append(s[i])
    return ans

s="(()())(())"
print(remove_paren(s))