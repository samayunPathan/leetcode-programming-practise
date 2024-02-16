def maximum_swap(num):
    ls=[i for i in str(num)]
    m=sorted(ls,reverse=True)
    return ''.join(m[:2])+str(num)[2:]


num=2736
print(maximum_swap(num))