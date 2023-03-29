def merge_item(item1,item2):
    d1=dict(item1)
    d2=dict(item2)
    l1=len(item1);l2=len(item2)
    if l1>l2:
        for i in range(len(l1)):
            


items1 = [[1,1],[4,5],[3,8]]; items2 = [[3,1],[1,5]]
print(merge_item(items1,items2))