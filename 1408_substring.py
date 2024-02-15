def sub_String(words):
    res=[]
    l=len(words)
    for i in range(l):
        for j in range(i+1,l):
            if words[j] in words[i]:
                res.append(words[j])
            if words[i] in words[j]:
                res.append(words[i])
    return res
words = ["mass","as","hero","superhero"]
words = ["leetcode","et","code"]
print(sub_String(words))