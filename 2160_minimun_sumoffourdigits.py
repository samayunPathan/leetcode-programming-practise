def minimum_sum(num):
    # s=list(str(num))
    # s.sort()
    # return int(s[0]+s[2])+int(s[1]+s[3])
    a = sorted(str(num)) 
    return int(a[0] + a[2]) + int(a[1] + a[3]) 
print(minimum_sum(2932))
m='2932'
n=list(str(m))
print(n)
n.sort()
print(n)