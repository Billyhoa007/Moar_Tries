import json
import string # Check if this module is needed / being used
import sys
import time # Check if this module is needed / being used
import datetime
from time import strptime
import shows
import records

__author__ = Chris

class show:
    def __init__(self, name, beginTime, endTime, dayofweek, counter):
        self.name = name
        self.begintTime = beginTime
        self.endTime = endTime
        counter = counter

class record:
    def __init__(self, ip, logTime, dayofweek,  ):
        self.ip = ip
            self.logTime, = logTime
                self.dayofweek = dayofweek

# I have no idea what I am doing...

################
# main program #
################
if __name__ == "__main__":

  try:
    data = sys.stdin.readlines() 
    for sl in data: # My goal for this loop is to keep a count of each show in log
      s = sl.split()
      logDateTime = s[3]
      logTime = whichHour(logDateTime)
      year, month, day = exactDay(logDateTime)
      dayofweek = dateToInt(year, month, day)
      whichShow(logTime, dayofweek)
    outputToConsole()
   
  except:
    pass
