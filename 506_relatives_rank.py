# def relative_rank(nums):
#     d={-1:"Gold Medal",-2:"Silver Medal",-3:"Bronze Medal"}
#     n=sorted(list(nums),reverse=True)
#     for i in range(len(n)):
#         d[n[i]]=i+1
#     print(d)
#     ls=[str(d[i]) for i in nums]
#     for i in range(len(ls)):
#         if ls[i]=='1':
#             ls[i]=d[-1]
#         elif ls[i]=='2':
#             ls[i]=d[-2]
#         elif ls[i]=='3':
#             ls[i]=d[-3]
#     return ls

# m=[10,3,8,9,4]
# s = [5,4,3,2,1]
# print(relative_rank(s))

n=123
m=str(n)
print(m.split(' '))

