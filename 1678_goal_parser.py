def goal_parser(s):
    temp='';res='';d={'G':'G','()':'o','(al)':'al'}
    for i in s:
        temp+=i
        if temp in d:
            res+=d[temp]
            temp=''
    return res
st="(al)G(al)()()G"
print(goal_parser(st))





















# def goal_parser(s):
#     n=''
#     l=str(s.split(')'))
#     l2=''.join(l)
#     print(l2)
#     ls=l.split('(')
#     print(ls)

#     for i in l:
#         if i=='(G' or i== 'G':
#             n+='G'
#         elif i=='(':
#             n+='o'
#         elif i=='(al':
#             n+='al'
       
#     return n
# st="(al)G(al)()()G"
# print(goal_parser(st))