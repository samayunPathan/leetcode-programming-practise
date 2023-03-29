def capita_title(s):
    s=s.split(' ');res=[]
    for i in s:
        if len(i)>2:
            res.append(i.title())
        else:
            res.append(i)
    return ' '.join(res)

t= "First leTTeR of EACH Word"
print(capita_title(t))