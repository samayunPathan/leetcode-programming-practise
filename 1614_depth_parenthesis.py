def depth_paren(s):
    d={')':'('};stack=[]
    for i in s:
        if i in d.values():
            stack.append(i)
        else:
            if stack or stack[-1]==i:
                stack.pop()
    return stack

s = "(1+(2*3)+((8)/4))+1"
print(depth_paren(s))