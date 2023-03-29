# for i in range(1,7):
#     print(i*'1')

for i in range(3):
    for j in range(i+1):
        print('1',end='')
    print('')

# def piramid(n):
#     if n==0:
#         return False
#     else:
#         piramid(n-1)
#         print('*'*n)
# print(piramid(4))

for i in range(3):
    for j in range(i+1):
        print(' ',end='')
    print('1')