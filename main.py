#!/usr/bin/python

import string # Check if this module is needed / being used
# import sys
import time # Check if this module is needed / being used
import datetime
from time import strptime
import functions
# import libraries

__author__ = 'Chris'


################
# main program #
################
if __name__ == "__main__":

  try:
    showArray = []
    logdata = sys.stdin.readlines()

    # My goal for this loop is to create a new object for each record
    for log in logdata:
      s = log.split()
      ip = s[0]
      logDateTime = s[3]
      logTime = functions.whichHour(logDateTime)
      year, month, day = functions.exactDay(logDateTime)
      dayofweek = functions.dateToInt(year, month, day)
      
      i = 0
      object[i] = record([ip, logTime, dayofweek]) # attempting to pass these values into the object
      i += 1
      showArray[i] = object[i] # store object in array
    
    print showArray[0]

  # Process the information, instantiate a new object, put in array, compare and then output to console / wherever.
   
  except:
    pass
