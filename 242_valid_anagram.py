from multiprocessing.dummy import active_children


s='rat';t='car'
def valid(s,t):
    sum1=0;sum2=0
    for i in range(len(s)):
        sum1+=ord(s[i])
        sum2+=ord(t[i])
    return ['false','true'][sum1==sum2]
print(valid(s,t))

# if len(s) != len(t):
#     return False
# elif sorted(s) == sorted(t):
#     return True
# else:
#     return False