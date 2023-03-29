def relative(arr1,arr2):
    res=[];i=0;j=0
    while i<len(arr2):
        res.extend([arr2[i]]*arr1.count(arr2[i]))
        i+=1
    ns=sorted(list(set(arr1)-set(res)))
    while j<len(ns):
        res.extend([ns[j]]*arr1.count(ns[j]))
        j+=1
    return res

        
    
    
arr1 = [2,3,1,3,2,4,6,7,9,2,19,19]; arr2 = [2,1,4,3,9,6]
print(relative(arr1,arr2))
