def rev_s(s):
    n='';s=s.split(' ')
    print(s)
    for i in s:
        n+=i[::-1]
        n+=' '
    return n
s="Let's take LeetCode contest"
print(rev_s(s))

# print('shanto'[::-1])