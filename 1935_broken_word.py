def broken_word(s,b):
    c=0;b=[*b]
    s=s.split(' ')
    for i in s:
        if any(j in b for j in i):
            continue
        else:
            c+=1
    return c
    
    

text = "hello world"
brokenLetters = "ad"
print(broken_word(text,brokenLetters))