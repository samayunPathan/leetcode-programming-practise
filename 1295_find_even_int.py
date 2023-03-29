def find_even(nums):
    return len([i for i in nums if len(str(i))%2==0])

n=[12,345,2,6,7896]
print(find_even(n))