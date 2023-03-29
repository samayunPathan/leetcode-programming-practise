def count_common(word1,word2):
    res=0
    for i in word1:
        if word1.count(i) == word2.count(i)==1:
            res+=1
    return res
words1 = ["leetcode","is","amazing","as","is"]; words2 = ["amazing","leetcode","is"]
print(count_common(words1,words2))