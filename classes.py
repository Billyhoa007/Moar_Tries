class show:
    def __init__(self, name, beginTime, endTime, dayofweek, counter):
        self.name = name
        self.begintTime = beginTime
        self.endTime = endTime
        self.counter = counter

class record:
    def __init__(self, ip, logTime, dayofweek):
        self.ip = ip
        self.logTime, = logTime
        self.dayofweek = dayofweek

    def printRecord(self):
        for line in self.ip:
            print line

# I have no idea what I am doing...