pairs={')':'(','}':'{',']':'['}
print(pairs[')'])
stack=[]
if not stack:
    print('yes')
else:
    print('no')

def check_parathesis(n):
    stack=[];d={')':'(','}':'{',']':'['}
    for i in n:
        if i in d.values():
            stack.append(i)
        elif stack or d[i]==stack[-1]:
            stack.pop()
        else:
            return False
    return not stack
s=['[',']','(']
print(check_parathesis(s))