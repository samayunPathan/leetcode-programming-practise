def day_of(s):
    day=int(date[-2:])
    month=int(date[5:7])
    year=int(date[:4])
    
    year_list=[0,31,59,89,120,150,181,211,242,272,303,333]
    
    if year%4==0 and year!=1900 and month>2:
        day+=1
    return year_list[month-1]+day


date = "2019-01-09"
print(day_of(date))