def great_letter(s):
    # n=s.lower();l=""
    # for i in n:
    #     if n.count(i)>=2:
    #         if i.upper() in s and i in s:
    #             l+=i
    # if len(l)==0:
    #         return " "
    # else:
    #     l=sorted(l)
    #     return l[-1].upper()

    new = ""
        
    for i in s:
        if i.isupper() and i.lower() in s:
            if i>new:
                print(i)
                new = i.upper()
                        
    return new
s = "arRAzFif"
print(great_letter(s))

if 'r'>'z':
    print('yes')
    