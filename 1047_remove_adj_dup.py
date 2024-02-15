def remove_aj(s):
    # stack=[]
    # for i in s:
    #     if len(stack)!=0 and i in stack:
    #         print(i)
    #         stack.remove(i)
    #     else:
    #         stack.append(i)
    # return ''.join(stack)
    stack = []
    for char in s:
        if stack and char==stack[-1]:
            stack.pop()

        else:
            stack.append(char)
        
    return ''.join(stack)
s = "aababaab"
# print(remove_aj(s))  
s=[]      
for i in range(3):
    s.append(input('enter : '))

print(s)