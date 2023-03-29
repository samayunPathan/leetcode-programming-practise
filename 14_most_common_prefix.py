strs=['a']
l=''
if len(strs)>3:
    for i in range(len(strs)-2):
        for j in range(len(strs)):
            if strs[i][j]==strs[i+1][j]==strs[i+2][j]:
                l+=strs[i][j]
if len(strs)<2:
    