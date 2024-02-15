def longest_pre(strs):
    s=sorted(strs)
    n=''
    first=s[0]
    last=s[-1]
    for i in range(min(len(first),len(last))):
        if first[i]!=last[i]:
            return n
        n+=first[i]
    return n

strs = ["flower","flow","flight"]
print(longest_pre(strs))