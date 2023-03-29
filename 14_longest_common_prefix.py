def logestest_word(nums):
    length=len(nums);n=''
    for i in range(length):
        for j in nums[i]:
            print(j)
            if j in n[i]:
                print(nums[i])
                n+=j
    return n
ls=['flow','flaws','flat']
print(logestest_word(ls))