def reverse_s(s):
    # return [s[~i] for i in range(len(s))]
    i=0
    while i<len(s)//2:
        k=s[i]
        s[i]=s[~i]
        s[~i]=k
        i+=1
    return s


s = ["h","e","l","l","o"]
print(reverse_s(s))