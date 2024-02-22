def reverseWords(s: str) -> str:
        s=s.split()
        temp=[]
        for i in range(len(s)-1,-1,-1):
            temp.append(s[i])
            
        return ' '.join(temp)
s='hello world'
print(reverseWords(s))