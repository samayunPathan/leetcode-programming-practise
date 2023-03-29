nums=[1,2,3,4]
# l=set(l)
# print(l)
# print(['False','True'][sum(set(l))!=sum(l)])
def re(num):
    return['true','false'][sum(set(num))==sum(num)]
    # return ['y','s'][10<0]
print(re(nums))
# print(['y','s'][10<20])