def count_good(arr,a,b,c):
    l=len(arr);res=0
    # for i in range(l):
    #     j=i+1
    #     k=l-1
    #     while j<k:
    #         if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
    #             res+=1
    #             j+=1
    #         else:
    #             k-=1
                
            
                
    # return res 
    for i in range(l):
        for j in range(i+1,l):
            for k in range(j+1,l):
                if abs(arr[i]-arr[j])<=a and abs(arr[j]-arr[k])<=b and abs(arr[i]-arr[k])<=c:
                    res+=1
    return res

arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
print(count_good(arr,a,b,c))