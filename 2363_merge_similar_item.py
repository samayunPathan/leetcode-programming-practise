def merge_item(items1,iems2):
    d={}
    for i in items1:
        d[i[0]]=i[1]
    for i in items2:
	    if i[0] in d:
            d[i[0]]+=i[1]
        d[i[0]]=i[1]
    return d
            
    



    

items1 = [[1,1],[4,5],[3,8]]
items2 = [[3,1],[1,5]]
print(merge_item(items1,items2))


