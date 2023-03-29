def decrypt(s):
    res=[];i=0
    while i<len(s):
        if i+2<len(s) and s[i+2]=='#':
            val=int(s[i:i+2])
            res.append(chr(val+96)) # chr(65-90)-> A-Z chr(97-122)-> a-z
            i+=3
        else:
            res.append(chr(int(s[i])+96))
            i+=1
    return ''.join(res)


s = "10#11#12"
print(decrypt(s))