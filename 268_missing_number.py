def missing_number(nums):
   l=len(nums)
   l1=list(range(0,l+1))
   return sum(l1)-sum(nums)
l=[1,0]
print(missing_number(l))

