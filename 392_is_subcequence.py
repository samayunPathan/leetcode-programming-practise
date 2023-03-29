def is_sub(s,t):
    s=list(set(s));t=list(set(t))
    if all([i for i in s if i in t]):
        return True
    return False
# s = "abc";t = "ahbgdc"
s = "axc"; t = "ahbgdc"
print(is_sub(s,t))