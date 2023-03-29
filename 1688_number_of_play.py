def play_match(num):
    res=0
    while num>1:
        if num%2==0:
            res+=num//2
            num=num//2
        else:
            res+=(num-1)//2
            num=((num-1)//2)+1
            
    return res
   
print(play_match(14))
