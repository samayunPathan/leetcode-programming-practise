def single_no(nums):
    return [i for i in nums if nums.count(i)==1][0]
    

nums =[4,1,2,1,2]
print(single_no(nums))