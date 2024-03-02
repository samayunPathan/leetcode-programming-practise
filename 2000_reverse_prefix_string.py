def reverse_prefix(word,ch):
    c=0;i=0
    for i in word:
        if i==ch:
            break
            
        c+=1
    return ch+word[:c][::-1]+word[c+1:] if ch in word else word
word='abcdefd'
ch='d'
print(reverse_prefix(word,ch))