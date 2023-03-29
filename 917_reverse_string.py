def rev_s(s):
    d={};ind=0
    for i in s:
        if i.isalpha()==False:
            d[ind]=i
        ind+=1
    temp=[i for i in s if i.isalpha()][::-1]
    for i in d:
        temp.insert(i,d[i])
    return ''.join(temp)


s="a-bC-dEf-ghIj"
print(rev_s(s))

k=2%10
print(k)

# name='shanto'
# # name[1]='p'
# print(name[1])