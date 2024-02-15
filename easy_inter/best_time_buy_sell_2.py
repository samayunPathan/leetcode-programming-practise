def best_bs(prices):
    res=0
    for i in range(len(prices)-1):
        if prices[i]<prices[i+1]:
            res+=prices[i+1]-prices[i]
        # i+=1
    return res

prices = [7,1,5,3,6,4]
print(best_bs(prices))