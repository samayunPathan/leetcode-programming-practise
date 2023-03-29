def rotate_s(s,goal):
    n,k=[*s],[*goal]
    for i in range(len(n)):
        j=n[0]
        n.pop(0)
        n.append(j)
        if n==k:
            return True
    return False
print(rotate_s("abcde","cdeab"))

# s='hello'
# n=[*s]
# print(n)


