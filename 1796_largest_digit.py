def largest_digit(s):
    # s=[*s];res=[]
    # for i in s:
    #     if not i.isalpha():
    #         res.append(i)
    # ls=list(map(int,res))
    # if len(set(ls))==1:
    #     return -1
    # else:
    #     m=max(ls)
    #     ls.remove(m)
    #     return max(ls)

     output = []
        
        for l in s:
            if l.isdigit():
                output.append(int(l))
                
        output = sorted(list(set(output)))
        if len(output) < 2: return -1
        
        return output[-2]

s = "dfa111afd"
print(largest_digit(s))