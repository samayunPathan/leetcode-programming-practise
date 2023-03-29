def check(s):
    stack=[]
    pairs={')':'(','}':'{',']':'['}
    for i in s:
        if i in pairs.values():
            stack.append(i)
        else:
            if not stack or stack[-1]!=pairs[i]:
                return False
            else:
                stack.pop()
    return not stack
s=[']']
print(check(s))