def destination_city(nums):
    s=set(i[0] for i in nums)
    for i in nums:
        if i[1] not in s:
            return i[1]

paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
print(destination_city(paths))