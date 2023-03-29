# def sort_people(names,heigths):
#     d={}
#     for i in range(len(names)):
#         d[names[i]]=heigths[i]
#     return d
name=['shanto','pranto','pathan']
height=[170,165,180]
# print(sort_people(name,height))

print(height.index(180))
def sort_p(names,heights):
    tempLi = sorted(heights)
    ans = []
    for i in tempLi:
        ans.append(names[heights.index(i)])
    return ans
print(sort_p(name,height))
