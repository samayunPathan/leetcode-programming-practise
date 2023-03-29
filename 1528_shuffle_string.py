li=[4,5,6,7,0,2,1,3]
def shuffle_string(s,l):
    shuffled=[None]*len(s)
    for i in range(len(s)):
        shuffled[l[i]]=s[i]
    return shuffled
    # return ''.join(shuffled)
print(shuffle_string('codeleet',li))

# s='codeleet'
# shu=[None]*len(s)
# shu[li[0]]=s[0]
# print(shu)
l=[None]*5
l[2]=5
print(l)