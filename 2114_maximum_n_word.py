s = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]
def maximum_word(sentences):
    s=[];ls=[]
    for i in sentences:
        s=i.split(' ')
        len([s])
        ls.append(len(s))
        s=[]
    return max(ls)
print(maximum_word(s))