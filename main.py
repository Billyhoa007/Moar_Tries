#!/usr/bin/python

# import json
import string # Check if this module is needed / being used
import sys
import time # Check if this module is needed / being used
import datetime
from time import strptime
# import functions
# import libraries

__author__ = 'Chris'


################
# main program #
################
if __name__ == "__main__":

  try:
    logdata = sys.stdin.readlines()

    # My goal for this loop is to keep a count of each show in log
    for sl in data:
      s = sl.split()
      logDateTime = s[3]
      logTime = records.whichHour(logDateTime)
      year, month, day = records.exactDay(logDateTime)
      dayofweek = records.dateToInt(year, month, day)
      shows.whichShow(logTime, dayofweek)
    
    outputToConsole()

  # Process the information, instantiate a new object, put in array, compare and then output to console / wherever.
   
  except:
    pass
