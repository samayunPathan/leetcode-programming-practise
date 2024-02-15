
def remove_out(s):
    stack=''
    start=0
    count=0
    for i in range(len(s)):
        if s[i]=='(':
            count+=1
        if s[i]==')':
            count-=1
        if count==0:
            stack+=s[start+1:i]
            start=i+1

    return stack
s = "(()())(())(()(()))"
print(remove_out(s))
