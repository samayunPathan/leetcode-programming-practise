def count_item(n,ruleKey,ruleValue):
    d={'type':0,'color':1,'name':2};c=0
    k=d[ruleKey]
    for i in n:
        if i[k]==ruleValue:
            c+=1
    return c

items = [["phone","blue","pixel"],["computer","silver","lenovo"],["phone","silver","iphone"]]
items2=[["phone","blue","pixel"],["computer","silver","phone"],["phone","gold","iphone"]]
items3=[["ii","iiiiiii","ii"],["iiiiiii","iiiiiii","ii"],["ii","iiiiiii","iiiiiii"]]
ruleKey = "color"
ruleValue = "ii"
print(count_item(items2,ruleKey,ruleValue))
