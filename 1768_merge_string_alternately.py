def func(l,word1,word2):
    s=''
    for i in range(l):
        s+=word1[i]
        s+=word2[i]
    return s
def merge_s(word1,word2):
    if len(word1)<len(word2):
        l=len(word1)
        s=func(l,word1,word2)
        return s+word2[len(word1):]
    else:
        l=len(word2)
        s=func(l,word1,word2)
        return s+word1[len(word2):]
    
   


    
word1 = "ab"
word2 = "pqrs"
word1 = "abcd"
word2 = "pq"
print(merge_s(word1,word2))