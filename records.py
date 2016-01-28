################################################
# This function returns a log date as an integer
################################################
def dateToInt(year, month, day):
    dayofweek = datetime.date(year, month, day).isoweekday()
        return dayofweek

####################################################
# This function finds the hour the log was generated
####################################################
def whichHour(logDateTime):
    logTime = logDateTime[13:15] # the hour is within this index range
    return logTime # return the hour of the log generation

##################################
# Return year month and day values
##################################
def exactDay(logDateTime):
    yearstr = logDateTime[8:12]
    monthStr = logDateTime[4:7]
    daystr = logDateTime[1:3]
    monthnum = strptime(monthStr,'%b').tm_mon
    year = int(yearstr)
    month = int(monthnum)
    day = int(daystr)
    return year, month, day # return list with these values? or just return them?