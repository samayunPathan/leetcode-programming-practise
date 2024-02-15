def first_cha(s):
    for i in range(len(s)):
        if s.count(s[i])==1:
            return i
       
    return -1

s = "loveleetcode"
print(first_cha(s))
