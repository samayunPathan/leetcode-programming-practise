# def sum_diff(nums):
    # l=len(nums)
    # ans=[None]*l
    # for i in range(l):
    #     left_s=sum(nums[:i])
    #     print(left_s)                          leetcode doesn't support 
    #     right_s=sum(nums[i+1:])
    #     print(right_s)
    #     ans[i]=abs(left_s-right_s)
    # return ans


def sum_diff(nums):
    prefix=0
    suffix=sum(nums)
    ans=[None]*len(nums)
    for i in range(len(nums)):
        prefix+=nums[i]
        ans[i]=abs(prefix-suffix)
        suffix-=nums[i]
    return ans




nums = [10,4,8,3]
print(sum_diff(nums))


