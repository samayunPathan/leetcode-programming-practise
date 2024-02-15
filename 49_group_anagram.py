l=["eat","tea","tan","ate","nat","bat"]
# def valid_ana(strs):
#     lr=[]
#     for i in range(len(strs)):
#         for j in range(i+1,len(strs)):
#             if sorted(strs[i])==sorted(strs[j]):
#                 lr.append(strs[j])
            
                
#     return tuple(lr)
# print(valid_ana(l))

def valid_anag(strs):
    d={}
    for i in range(len(strs)):
        x=''.join(sorted(strs[i]))
        print(x)
        if x not in d:
            d[x]=[strs[i]]
        else:
            d.get(x).append(strs[i])
            
            
    return d.values()
        

def group_ana(strs):
    res=[];a=[]
    for i in range(len(strs)):
        for j in range(i+1,len(strs)):
            if sorted(strs[i])==sorted(strs[i]):
                a.append(strs[i])
            print(a)
   
    
        

# print(valid_anag(l))
print(group_ana(l))
# dict_s={
#     'name':'samayun',
#     'name':'pranto',
#     'age': 23
# }
# print(dict_s)

# strin='print'
# c=sorted(strin)
# d=''.join(c)
# print(c)
# print(d)

