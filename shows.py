shows = [
         "the Shannon Steele Show",
         "the Herd-Will Geoff Show",
         "the Vinnie's Midday Show",
         "the Aleister and Maggie Show",
         "the Steve Jones Show",
         "the Eye on the Target Radio Show",
         "the Handy Randy Show",
         "the Brian 'Moonshine' Varner Show",
         "the Best Stams Sports Show",
         "the TJ Dylan Show",
         "Some Kind of Radio Show",
         "the Frenemies News Radio Show",
         "the Zal & Zera Game Forum",
         "the Undaground Wrestling Show",
         "the Altered Realm Show",
         "the Bob Fritz Show",
         "the Sports to the Max Show",
         "Laura Lyn's Psychic Power Show",
         "an undesignated time slot"
         ]

# For a CGI interface, you will have to store the values in a database / pull these values from DB
# CREATE TABLE SHOWS;

# Show name, begin time, end time, day (numerical or convert: monday = 1, tuesday = 2)

# It will search the database for dpulicate entires / new show times and update (how? dunno the comparison SQL)

slots = {
    slot1: [beginTime, endTime]
}


showCounters = { # programatically create these? Yes?
    'counter0' : 0,
    'counter1' : 0,
    'counter2' : 0,
    'counter3' : 0,
    'counter4' : 0,
    'counter5' : 0,
    'counter6' : 0,
    'counter7' : 0,
    'counter8' : 0,
    'counter9' : 0,
    'counter10' : 0,
    'counter11' : 0,
    'counter12' : 0,
    'counter13' : 0,
    'counter14' : 0,
    'counter15' : 0,
    'counter16' : 0,
    'counter17' : 0,
    'counter18' : 0
}

#######################################################################################
# I hard coded the show names and corresponding slots for clarity in their relationship
# An interface or section of code might later be created for faster edits
#######################################################################################

def whichShow(strlogTime, strdayofweek):
    logTime = int(strlogTime)
        dayofweek = int(strdayofweek)
            if logTime in range(6,9) and dayofweek in range(1,5):
#   print "This is the Shannon Steele Show" # Will pass in function
showCounters['counter0'] += 1
    elif(logTime in range(9,12) and dayofweek in range(1,5)):
    #   print "This is the Herd-Will Geoff Show"
    showCounters['counter1'] += 1
        elif(logTime in range(12,15) and dayofweek in range(1,5)):
#   print "This is Vinnie's Midday Show"
showCounters['counter2'] += 1
    elif(logTime in range(15,18) and dayofweek in range(1,5)):
    #   print "This is the Aleister and Maggie Show"
    showCounters['counter3'] += 1
        elif(logTime in range(19,23) and dayofweek == 3):
#   print "This is the Steve Jones Show"
showCounters['counter4'] += 1
    elif(logTime in range(19,22) and dayofweek == 1):
    #   print "This is the Eye on the Target Radio Show"
    showCounters['counter5'] += 1
        elif(logTime in range(18,23) and dayofweek == 2):
#   print "This is the Handy Randy Show"
showCounters['counter6'] += 1
    elif(logTime in range(18,20) and dayofweek == 4):
    #   print "This is the Brian 'Moonshine' Varner Show"
    showCounters['counter7'] += 1
        elif(logTime in range(20,23) and dayofweek == 4):
#   print "This is the Best Stams Sports Show"
showCounters['counter8'] += 1
    elif(logTime in range(18,20) and dayofweek == 5):
    #   print "This is the TJ Dylan Show"
    showCounters['counter9'] += 1
        elif(logTime in range(20,24) and dayofweek == 5): #this one might break (no 24th hour)
#   print "This is Some Kind of Radio Show"
showCounters['counter10'] += 1
    elif(logTime in range(10,13) and dayofweek == 6):
    #   print "This is the Frenemies News Radio Show"
    showCounters['counter11'] += 1
        elif(logTime in range(15,17) and dayofweek == 6):
#   print "This is the Zal & Zera Game Forum"
showCounters['counter12'] += 1
    elif(logTime in range(17,19) and dayofweek == 6):
    #   print "This is the Undaground Wrestling Show"
    showCounters['counter13'] += 1
        elif(logTime in range(20,24) and dayofweek == 6): #another one with same issue
#   print "This is the Altered Realm Show"
showCounters['counter14'] += 1
    elif(logTime in range(14,17) and dayofweek == 7):
    #   print "This is the Bob Fritz Show"
    showCounters['counter15'] += 1
        elif(logTime in range(19,22) and dayofweek == 7):
#   print "This is the Sports to the Max Show"
showCounters['counter16'] += 1
    elif(logTime in range(22,24) and dayofweek == 7):
    #   print "This is Laura Lyn's Psychic Power Show"
    showCounters['counter17'] += 1
        else:
#   print "This is an undesignated time slot"
showCounters['counter18'] += 1
