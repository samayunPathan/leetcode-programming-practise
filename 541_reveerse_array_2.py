# st='abcd'
# def reverse_ar_2(s,k):
#     d=0
#     for i in range(0,k-1):
#         d=s[i]
#         s[i]=s[k-1-i]
#         s[k-1-i]=d
        
#     return s
# print(reverse_ar_2(st,2))

s='pranto'
def swap(s):
    d=0
    for i in range(len(s)):
        d=s[i]
        s[i]=s[len(s)-1-i]
        s[len(s)-1-i]=d
    return s
print(swap(s))