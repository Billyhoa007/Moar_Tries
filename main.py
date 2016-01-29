#!/usr/bin/python

# import json
import string # Check if this module is needed / being used
import sys
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

    # My goal for this loop is to keep a count of each show in log
    for log in logdata:
      s = log.split()
      ip = s[0]
      logDateTime = s[3]
      logTime = functions.whichHour(logDateTime)
      year, month, day = functions.exactDay(logDateTime)
      dayofweek = functions.dateToInt(year, month, day)
#     functions.whichShow(logTime, dayofweek)
      i = 0
      object[i] = record([ip, logTime, dayofweek])
      i += 1
      showArray[i] = object[i]
    print showArray[0]
    #    outputToConsole()

  # Process the information, instantiate a new object, put in array, compare and then output to console / wherever.
   
  except:
    pass
