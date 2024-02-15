def reverse_int(x):
   if x<0:
      n=str(x)
      n=n[1:]
      n='-'+n[::-1]
   else:
      n=str(x)
      n=n[::-1]

   return 0 if int(n)>=2**31-1 or int(n)<-2**31 else int(n)
    

   
 

x=-123
print(reverse_int(x))