def hamming_distance(x,y):
    x=format(x,'b')
    y=format(y,'b')
    res=0
    print(x)
    print(y)
    for i in range(min(len(x),len(y))):
        if x[i]!=y[i]:
            res+=1
    return res+(max(len(x),len(y))-min(len(x),len(y)))
x = 1 
y = 4
print(hamming_distance(14,4))