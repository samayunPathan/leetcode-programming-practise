def plus_one(l):
    l2=int(''.join(map(str,l)))+1
    return [int(i) for i in str(l2)]
ls=['1','2','3']
ls2=[1,2,3]
print(plus_one(ls2))

n='hellopranto'
print(n.split(''))