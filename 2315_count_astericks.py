def count_a(s):
    ns=s.split('|');c=0
    for i in range(0,len(ns),2):
        c+=ns[i].count('*')
    return c


n="l|*e*et|c**o|*de|"
m="yo|uar|e**|b|e***au|tifu|l"
print(count_a(m))