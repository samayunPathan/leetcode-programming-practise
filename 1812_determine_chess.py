def d_chess(s):
   return ord(s[0])%2!=int(s[1])%2
print(d_chess('a1'))