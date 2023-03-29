s="A man, a plan, a canal: Panama"
s2='race a car'
# print(s2.isalnum())
l=''.join(i for i in s2 if i.isalnum())
if l[::-1]==l:
    print(l)

def valid_palindrome(n):
    n=''.join(i for i in s2 if i.isalnum())
    t=n.lower()
    if t[::-1]==t:
        return True
    return False

print(valid_palindrome(s2))

# s='amanaplanacanalpanama'
# print(s[::-1])
# if s==s[::-1]:
#     print('true')
