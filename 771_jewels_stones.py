def stones(jeweles,stones):
    s=0
    for i in jeweles:
        s+=stones.count(i)
    return s
    
j= "aA"; s = "aAAbbbb"
print(stones(j,s))

