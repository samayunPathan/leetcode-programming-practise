def reformate(date):
    s = date.split() 
    d={'Jan':'01','Feb':'02','Mar':'03','Apr':'04','May':'05','Jun':'06','Jul':'07','Aug':'08','Sep':'09','Oct':'10','Nov':'11','Dec':'12'}
    day=s[0][:-2]
    mon=d[s[1]]
    if int(day)<10:
        day='0'+day

    return f'{s[2]}-{mon}-{day}'
   
date = "5th Jan 2052"
print(reformate(date))



# d={'jan':1,'feb':2,'mar':3,'apr':4,'may':5,'jun':6,'jul':7,'aug':8,'sep':9,'oct':10,'nov':11,'dec':12}
# s=['oct']
# n=s[0]
# print(d[n])
# s='shanto'
# print(s[:1])