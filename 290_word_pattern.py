def pattern_s(pattern,s):
    d={}
    word=s.split(' ')
    if len(pattern)!=len(word):
        return False
    if len(set(pattern))!=len(set(word)):
        return False
    for i in range(len(word)):
        if word[i] not in d:
            d[word[i]]=pattern[i]
        elif d[word[i]]!=pattern[i]:
            return False
    return True
pattern = "abba" 
s = "dog cat cat dog"
print(pattern_s(pattern,s))