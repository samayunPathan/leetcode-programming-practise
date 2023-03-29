def sorting_sen(s):
    res=s.split(' ')
    a=[None]*len(res)
    for i in res:
        a[int(i[-1])-1]=i[:-1]
    return ' '.join(a)

    

a='is2 sentence4 This1 a3'
print(sorting_sen(a))


# l=[1,2,3]
# l.insert(2,8)
# print(l)