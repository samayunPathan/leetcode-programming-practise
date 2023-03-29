def sum_zero(n):
    res =[]
    if n%2==0:
        for i in range(1,n//2+1):
            res.extend([i,~i+1])
    else:
        res.append(0)
        for i in range(1,n//2+1):
            res.extend([i,~i+1])

    return res
    # return range(1 - n, n, 2)

print(sum_zero(4))