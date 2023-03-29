def double_re(n):
    m=int(str(n)[::-1])
    return n==int(str(m)[::-1])

print(double_re(526))