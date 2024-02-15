# def is_sub(s,t):
#     s=list(set(s));t=list(set(t))
#     if all([i for i in s if i in t]):
#         return True
#     return False
# # s = "abc";t = "ahbgdc"
def is_subse(s,t):
    if len(s)<len(t):
        t=sorted(t)
        t=''.join(t)
        s=sorted(s)
        s=''.join(s)
        print(t)
        if s in t:
            return True
        return False
    elif len(s)==len(t):
        if s==t:
            return True
        return False

# s = "axc"; t = "ahbgdc"
# s = "abc"
# t = "ahbgdc"
s="abc"
t="acb"
s="twn"
t="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxtxxxxxxxxxxxxxxxxxxxxwxxxxxxxxxxxxxxxxxxxxxxxxxn"
print(is_subse(s,t))