def greatest_word(s):
    d={}
    for i in s:
        d[i]=ord(i.lower())
   
s = "lEeTcOdE"
print(greatest_word(s))