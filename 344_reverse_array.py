def reverse_a(s):
    # ls=[None]*len(s)
    # for i in range(len(s)):
    #     ls[~i]=s[i]
    # return ls
    n=len(s);d=0
    for i in range(n//2):
        d=s[i]
        s[i]=s[n-1-i]
        s[n-1-i]=d
    return s
l=["h","e","l","l","o"]
print(reverse_a(l))

