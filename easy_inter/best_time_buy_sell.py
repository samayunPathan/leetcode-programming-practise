# def best_bs(prices):
    # l=len(prices)-1
    # m=min(prices[:l])
    # print(m)
    # for i in range(len(prices)):
    #     if m==prices[i]:
    #         j=i
    # mx=max(prices[j:])
    # print(mx)
    # return mx-m

def best_bs(prices):
    p=0
    m=prices[0]
    for i in range(len(prices)):
        p=max(p,prices[i]-m)
        m=min(m,prices[i])
    return p

prices=[7,1,5,3,6,4]
# prices=[7,6,4,3,1]
prices=[2,4,1]
print(best_bs(prices))
    

