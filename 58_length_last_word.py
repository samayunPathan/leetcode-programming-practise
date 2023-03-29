def last_len(s):
    s=s.strip() # remove first and last whitespace
    l=s.split(' ')
    return len(l[-1])


s="   fly me   to   the moon  "
print(last_len(s))