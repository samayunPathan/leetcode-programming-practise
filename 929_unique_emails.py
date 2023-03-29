def unique_e(nums):
    res=[];c=0
    for i in nums:
        print(i)
        if i not in res:
            res.append(i)
            c+=1
    return c
n=['shant0@gmail.com','pranto@gmail.com','pathanshanto@gmail.com']
m=["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
print(unique_e(m))