def what_is_the_time(time_in_mirror):
    hours, minutes = map(int,time_in_mirror.split(':'))
    total_minutes = hours*60 + minutes
    mirrored_total_mins = 720 - total_minutes
    mirrored_mins = mirrored_total_mins%60
    mirrored_h = (mirrored_total_mins - mirrored_mins)//60

    if mirrored_h <= 0:
        mirrored_h = '12'
    elif mirrored_h < 10:
        mirrored_h = '0' + str(mirrored_h)
    else: 
        mirrored_h = str(mirrored_h)
        
    if int(hours) >= 12 and mirrored_mins > 0:
        print('debug')
        mirrored_h = '11'
        
    if mirrored_mins <10:
        mirrored_mins = '0' + str(mirrored_mins)
    else:
        mirrored_mins = str(mirrored_mins)
    
    return("%s:%s"%(mirrored_h,mirrored_mins))

    # Your code here
print(what_is_the_time("06:55"),"== 05:05")
print(what_is_the_time("06:55") == "05:05")
print(what_is_the_time("11:59"),"== 12:01")
print(what_is_the_time("11:59") == "12:01")
print(what_is_the_time("12:02"),"== 11:58")
print(what_is_the_time("12:02") == "11:58")
print(what_is_the_time("04:00"),"== 08:00")
print(what_is_the_time("04:00") == "08:00")
print(what_is_the_time("06:00"),"== 06:00")
print(what_is_the_time("06:00") == "06:00")
print(what_is_the_time("12:00"),"== 12:00")
print(what_is_the_time("12:00") == "12:00")
