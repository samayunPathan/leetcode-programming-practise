
def product_array(nums):
    ct=0;p=0;s=1;n=len(nums);ans=[]
    for i in range(n):
        if nums[i]==0:
            ct+=1
        else:
            s*=nums[i]
    if ct>=2:
        return [0]*n
    elif ct==0:
        for i in range(n):
            ans.append(s//nums[i])
    else:
        for i in range(n):
            if nums[i]!=0:
                ans.append(0)
            else:
                ans.append(s)
    return ans

s=[0,2,3,4]
print(product_array(s))