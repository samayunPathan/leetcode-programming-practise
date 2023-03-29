def kids_candies(candies,extraCandies):
    res=[];m=max(candies)
    for i in candies:
        if i+extraCandies>=m:
            res.append('True')
        else:
            res.append('False')
    return res

candies=[2,3,5,1,3] 
print(kids_candies(candies,3))