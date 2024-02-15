def reverse_string(s,k):
    res=''
    i=k-1
    for i in range(len(s)):
        res+=s[i::-1]
        print(s[i::-1])
        i+=2
    return res 

s = "abcdefg"
k = 2
print(reverse_string(s,k))
