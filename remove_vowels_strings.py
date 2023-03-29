vowel='aeiou'
s='i am a student of class 4'
s2='welcome to geeksforgeeks'
l=''
for i in s2:
    # print(i)
    if i not in vowel:
        l+=i

        # print(i)
        # l=s.replace(i,'')
print(l)
