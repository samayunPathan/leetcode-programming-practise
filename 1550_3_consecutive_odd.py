def con_odd(arr):
    c=0
    for i in arr:
        if i%2!=0:
            c+=1
            if c>=3:
                return True
        else:
            c=0
    return False
    

arr = [1,2,34,3,4,5,23,12]
print(con_odd(arr))
            
        