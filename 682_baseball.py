def baseball(s):
    res=[]
    for i in s:
        if i=="C":
            res.pop()
        elif i=="D":
            res.append(2*(res[-1]))
        elif i=="+":
            res.append(res[-1]+res[-2])
        else:
            res.append(int(i))
    return sum(res)
s = ["5","2","C","D","+"]
print(baseball(s))