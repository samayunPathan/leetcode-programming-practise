def alike(s):
    l=len(s);vol=['a','e','i','o','u']
    a=s[:l//2];b=s[(l//2):];ar=0;br=0
    print(a,b)
    for i in range(len(a)):
        if a[i] in vol:
            ar+=1
        if b[i] in vol:
            br+=1
    return ar ==br 

         
s = "textbook"
print(alike(s))