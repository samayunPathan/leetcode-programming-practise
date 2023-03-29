def cal_digit(s,k):
    for i in s[0:k]:
        print(s[i])
s = "11111222223"
k = 3
print(cal_digit(s,k))