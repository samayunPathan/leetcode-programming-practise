def bal_string(s):
    d={'L':0,'R':0};res=0
    for i in s:
        d[i]+=1
        if d['L']==d['R']:
            res+=1
    return res

s='LRLLRRLRL'
print(bal_string(s))