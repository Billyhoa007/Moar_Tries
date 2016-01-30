#!/usr/bin/python

import string
import sys
import time
import functions
from classes import record
import libraries
import classes

__author__ = 'Chris'


################
# main program #
################
if __name__ == "__main__":

#  try:
    i = 0
    showArray = [i]
    logdata = sys.stdin.readlines()

    # My goal for this loop is to create a new object for each record
    for log in logdata:
      s = log.split()
      
      # returns object data
      ip = s[0]
      logDateTime = s[3]
      logTime = functions.whichHour(logDateTime)
      year, month, day = functions.exactDay(logDateTime)
      dayofweek = functions.dateToInt(year, month, day)
          #print ip
      
      # Trying to iteratively create new objects with each pass through the loop
      object0 = classes.record(ip, logTime, dayofweek) # attempting to pass these values into the object
      i += 1
      print object0.ip
      showArray[i] = object[i] # store object in array
      

  # Process the information, instantiate a new object, put in array, compare and then output to console / wherever.
   
   #  except:

