nums=list(map(int,input().split()))
target=int(input())

def binary_search(n,m):
    n.sort()
    start=0
    end=len(n)-1
    if m<n[-1]:
        while(start<=end):
            mid=start+((end-start)//2)
            if m==n[mid]:
                return mid
            elif(m<n[mid]):
                end=mid-1
            elif(m>n[mid]):
                start=mid+1
    else:
        n.append(m)
        n.sort() 
        start=0
        end=len(n)-1
        
        while(start<=end):
            mid=start+((end-start)//2)
            if m==n[mid]:
                return mid
            elif(m<n[mid]):
                end=mid-1
            elif(m>n[mid]):
                start=mid+1       
print(binary_search(nums,target))
