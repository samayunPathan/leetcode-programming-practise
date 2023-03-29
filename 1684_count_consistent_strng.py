def consistent(allowed,words):
    # c=0
    # for i in words:
    #     cal=True
    #     for j in i:
    #         if j not in allowed:
    #             cal=False
    #     if cal:
    #         c+=1
    # return c
    return sum(all(j in allowed for j in i)for i in words)

allowed = "ab"
words = ["ad","aa","bd","aaab","baa","badab"]
print(consistent(allowed,words))